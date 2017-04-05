from django.contrib import admin

from .models  import Customer , Account ,Card , cashWallet , transactionMode , transactionType ,transactionCategory ,Transaction , forexWallet ,forexTransactions , financialGoal , Currency

# Register your models here.
admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(cashWallet)
admin.site.register(transactionMode)
admin.site.register(transactionType)
admin.site.register(transactionCategory)
admin.site.register(Transaction)
admin.site.register(forexWallet)
admin.site.register(forexTransactions)
admin.site.register(financialGoal)
admin.site.register(Currency)
