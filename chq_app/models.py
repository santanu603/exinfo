from django.db import models
from datetime import datetime 



# Create your models here.


class master(models.Model):

    choise_bank=[
        ('State Bank of India', 'State Bank of India'),
        ('Bandhan Bank', 'Bandhan Bank'),
        ('HDFC Bank', 'HDFC Bank'),
        ('IDBI Bank', 'IDBI Bank'),
        ('Axis Bank', 'Axis Bank'),
        ('Union Bank of India', 'Union Bank of India'),
        ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'),
        ('Indian Bank', 'Indian Bank'),
        ('Punjab National bank', 'Punjab National bank'),
        ('Bank of Baroda', 'Bank of Baroda'),
        ('Indian Overseas Bank', 'Indian Overseas Bank'),
        ('Central Bank of India', 'Central Bank of India'),
        ('Canara Bank', 'Canara Bank'),
        ('UCO Bank', 'UCO Bank'),
        ('ICICI Bank', 'ICICI Bank'),
        ('IDFC FIRST Bank', 'IDFC FIRST Bank'),
    ]

    choice_agent=[
        ('Goutam Halder', 'Goutam Halder'),
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Jeet Roy', 'Jeet Roy'),
        ('Raju Barui', 'Raju Barui'),
    ]

    choice_status=[
        ('Received', 'Received'),
        ('Cleared', 'Cleared'),
        ('Bounced', 'Bounced'),
        ('Cancelled', 'Cancelled'),
    ]

    client=models.CharField(max_length=100, null=False)
    amount=models.IntegerField(null=False)
    chq=models.CharField(max_length=10, default='C->')
    bank=models.CharField(max_length=50, choices=choise_bank, null=False)
    status=models.CharField(max_length=20, choices=choice_status, null=False)
    agent=models.CharField(max_length=25, choices=choice_agent, null=False)
    date=models.DateTimeField(default=datetime.now)
    remarks=models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f'Client: {self.client}   Status: {self.status}'




class order(models.Model):

    choice_agent=[
        ('Goutam Halder', 'Goutam Halder'),
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Jeet Roy', 'Jeet Roy'),
        ('Raju Barui', 'Raju Barui'),
    ]

    choice_delivery=[
        ('Delivered','Delivered'),
        ('Not Delivered','Not Delivered'),
        ('Cancelled','Cancelled'),
    ]

    choice_payment=[
        ('Cash Given','Cash Given'),
        ('Ondate Cheque Given','Ondate Cheque Given'),
        ('Postdate Cheque Given','Postdate Cheque Given'),
        ('Online NEFT','Online NEFT'),
        ('UPI Payment','UPI Payment'),
        ('No Payment','No Payment'),
    ]

    choice_delivery_agent=[
        ('Kaka','Kaka'),
        ('Raju Barui','Raju Barui'),
        ('Rituraj Saran', 'Rituraj Saran'),
    ]

    date=models.DateTimeField(default=datetime.now)
    shop_name=models.CharField(max_length=80, null=False)
    invoice=models.CharField(max_length=11,default='I->', null=False)
    amount=models.IntegerField(null=False)
    agent=models.CharField(max_length=25, choices=choice_agent, null=False)
    deliverysts=models.CharField(max_length=25,choices=choice_delivery,null=False)
    deliveryagt=models.CharField(max_length=25,choices=choice_delivery_agent, null=False)
    paymentsts=models.CharField(max_length=50,choices=choice_payment, null=False)
    remarks=models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f'Client: {self.shop_name}   Delivery Status: {self.deliverysts} Payment Status: {self.paymentsts}'



class replacement(models.Model):


    choice_agent=[
        ('Goutam Halder', 'Goutam Halder'),
        ('Tinku Das', 'Tinku Das'),
        ('Biswajit Sanyal', 'Biswajit Sanyal'),
        ('Rituraj Saran', 'Rituraj Saran'),
        ('Jeet Roy', 'Jeet Roy'),
        ('Raju Barui', 'Raju Barui'),
    ]

    choice_status=[
        ('Received','Received'),
        ('CN Given','CN Given'),
        ('Item Given','Item Given'),
        ('DOA Received','DOA Received'),
        ('DOA Given','DOA Given'),
    ]

    date=models.DateTimeField(default=datetime.now)
    recv_challan=models.CharField(max_length=8, blank=True)
    client=models.CharField(max_length=30, null=False)
    item=models.CharField(max_length=30,null=False)
    qty=models.IntegerField(null=False)
    agent=models.CharField(max_length=25,choices=choice_agent, null=False)
    status=models.CharField(max_length=15,choices=choice_status, null=False)
    issue=models.CharField(max_length=100,blank=True)
    delv_doc=models.CharField(max_length=10,blank=True)
    delv_date=models.CharField(max_length=12,blank=True)
    remarks=models.CharField(max_length=80,blank=True)

    def __str__(self):
        return f'Client: {self.client}   status: {self.status}'