from django.shortcuts import render,HttpResponse,redirect
from .models import Record,Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required


#預設根目錄 D:\Django_Project\app\templates

# Create your views here.
@login_required
def hello(request):
	return render(request,'app/hello.html',{})

@login_required
def frontpage(request):
	
	record_form = RecordForm(initial={'balanceType':'支出'})

	#先把Record物件內所有的資料取出
	records = Record.objects.filter()

	income_list = [ record.cash for record in records if record.balanceType=='收入']
	outcome_list = [ record.cash for record in records if record.balanceType=='支出']

	income = sum(income_list) if len(income_list)!=0 else 0
	outcome = sum(outcome_list) if len(outcome_list)!=0 else 0

	net = income - outcome

	# return render(request,'app/index.html',
	# 	         {'records': records,'income':income,'outcome':outcome,'net':net})

	return render(request,'app/index.html',locals())

@login_required
def settings(request):
	categories = Category.objects.filter()

	return render(request,'app/settings.html',locals())

@login_required
def addCategory(request):
	if request.method=='POST':
		#返回的post_data為dictionary類型
		posted_data=request.POST
		#對應到settings.py的<input type="text" name="add_category" method="post">  name屬性
		category=posted_data['add_category']

    	
		#第一個category是models.py內定義的class內的屬性
		Category.objects.get_or_create(category=category)
		#在寫入資料庫後，重新導向頁面到/settings
		return redirect('/settings')

@login_required
def addRecord(request):
	if request.method=='POST':
		form=RecordForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('/')

@login_required
def deleteRecord(request):
	if request.method=='POST':
		id = request.POST['delete_val']
		Record.objects.filter(id=id).delete()
	return redirect('/')