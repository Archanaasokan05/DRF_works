
from django.shortcuts import render
from rest_framework import status, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from expenses.serializers import ExpenseSerializer


# Create your views here.
# API View for creating a user expense
class ExpenseCreate(APIView):
    authentication_classes = [TokenAuthentication]  # to check whether the requested user is valid or not
    permission_classes = [IsAuthenticated]  # only logged-in user can create expense
    def post(self,request):
        serializer_instance=ExpenseSerializer(data=request.data)
                                        # title,amount,category,payment,priority
                                        # all fields except user
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# API View for reading all expenses of a user
from expenses.models import Expense
class ExpenseList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        e=Expense.objects.filter(user=request.user) # filter only current user expenses
        serializer_instance=ExpenseSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)




from expenses.models import Expense
from django.shortcuts import get_object_or_404
from expenses.permissions import IsOwner

class RetrieveUpdateDeleteExpense(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]

    # retrieve an expense
    def get(self,request,pk):
        e=get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,e)
        serializer_instance=ExpenseSerializer(e)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # update an expense
    def put(self, request, pk):
        e = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,e)    # manually checks if requested user has permissions to perform the following operation
        serializer_instance = ExpenseSerializer(instance=e, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data, status=status.HTTP_400_BAD_REQUEST)

    # delete expense
    def delete(self, request, pk):
        e = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,e)    # manually checks if requested user has permissions to perform the following operation
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.db.models import Sum
from datetime import datetime
class ExpenseSummary(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # find todays date
        today_date=datetime.now().date()
        response_data={
            'todays_total':0
        }

        # find queryset
        qs=Expense.objects.filter(user=request.user,created__date=today_date)
        # find aggregate
        if qs:
            todays_total=qs.aggregate(total=Sum('amount')).get('total')

        # annotate(category wise)
            category_total=qs.values('category').annotate(total=Sum('amount'))
            response_data['todays_total']=todays_total
            response_data['category_total']=category_total
        month=datetime.now().month
        year=datetime.now().year
        u=request.user
        qs=Expense.objects.filter(user=u,created__month=month,created__year=year)
        if qs:
            monthly_total=qs.aggregate(total=Sum('amount')).get('total')
            # annotate(category wise)
            monthlycategory_total=qs.values('category').annotate(total=Sum('amount'))

            response_data['monthly_total'] = monthly_total
            response_data['monthlycategory_total'] = monthlycategory_total

        # return Response
        return Response(response_data,status=status.HTTP_200_OK)
