from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Customer(models.Model):
    CustomerID = models.CharField(max_length = 250 , default = 'NULL')
    Name = models.CharField(max_length = 250 , default = 'NULL')
    Address = models.CharField(max_length = 250 , default = 'NULL')
    #  = models.CharField(max_length = 250 , default = 'NULL')
    behaviourScore = models.IntegerField(max_length = 250 , default = 0)
    # playid = models.CharField(max_length = 250 , default = 'NULL')
    # playurl = models.URLField(max_length = 250 , default = 'NULplayL')

    def __str__(self):
        return self.CustomerID

class Account(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    accountNumber=models.CharField(max_length = 250 , default = 'NULL')
    Branch = models.CharField(max_length = 250 , default = 'NULL')
  
    def __str__(self):
        return self.accountNumber

class Card(models.Model):
    cardNumber=models.CharField(max_length = 250 , default = 'NULL')
    # Limit = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Limit = models.CharField(max_length = 250 , default = 'NULL')
    Account = models.ForeignKey(Account, on_delete=models.CASCADE , blank=True, null=True ) #account from which transaction is made .if cash this will be Null.


    Type = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.cardNumber   

class loansPolicies(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ID=models.CharField(max_length = 250 , default = 'NULL')
    Installment = models.CharField(max_length = 250 , default = 'NULL')
  
    def __str__(self):
        return self.accountNumber             

class cashWallet(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Balance = models.IntegerField(max_length = 250 , default = 0)
    # pid = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        Balance1 = str(self.Balance)
        return Balance1

class transactionMode(models.Model):
    Mode = models.CharField(max_length = 250 , default = 'Cash') # cash , card net banking etc

    def __str__(self):
        return self.Mode

class transactionType(models.Model):
    Type = models.CharField(max_length = 250 , default = 'Credit') # credit or debit 

    def __str__(self):
        return self.Type        

class transactionCategory(models.Model):
    Category = models.CharField(max_length = 250 , default = 'NULL') # food , luxury , entertainment etc.


    def __str__(self):
        return self.Category


class Transaction(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Type = models.ForeignKey(transactionType, on_delete=models.CASCADE  )
    TransactionID = models.CharField(max_length = 250 , default = 'NULL')
    Category = models.ForeignKey(transactionCategory, on_delete=models.CASCADE)
    Mode = models.ForeignKey(transactionMode, on_delete=models.CASCADE )
    Date = models.CharField(max_length = 250 , default = 'NULL')
    Time = models.CharField(max_length = 250 , default = 'NULL')
    Account = models.ForeignKey(Account, on_delete=models.CASCADE , blank=True, null=True ) #account from which transaction is made .if cash this will be Null.
    Card = models.ForeignKey(Card, on_delete=models.CASCADE , blank=True, null=True ) #card from which transaction is made .if cash this will be Null.
    Location = models.CharField(max_length = 250 , default = 'NULL')

    def __str__(self):
        return self.TransactionID

class Currency(models.Model):
    Currency = models.CharField(max_length = 250 , default = 'NULL') # food , luxury , entertainment etc.


    def __str__(self):
        return self.Currency        


class forexWallet(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Balance = models.IntegerField(max_length = 250 , default = 0) 
    Currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.Balance)





class forexTransactions(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Ammount = models.IntegerField(max_length = 250 , default = 0) 
    Currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.Ammount)


class financialGoal(models.Model):
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)

    Ammount = models.CharField(max_length = 250 , default = 'NULL') 
    # timeFrame = models.ForeignKey(Customer, on_delete=models.CASCADE) #in days
    timeFrame = models.CharField(max_length = 250 , default = 'NULL') 

