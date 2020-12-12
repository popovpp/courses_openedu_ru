import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool
from multiprocessing import current_process
from .models import Course


def get_html1(url):
	html_str = ''
	flag_try = 0
	while html_str == '' and flag_try <=4:
		try:
			new_html = urlopen(url, timeout=10)
			html_str = str(new_html.read(), encoding='utf-8')
		except Exception:
			print('error download')
			flag_try = flag_try + 1
	return html_str



def get_courses(searchWords=''):
	url = 'https://openedu.ru/course/'
	ahtml = get_html1(url)
	lst = re.findall(r'COURSES\s*=\s*(.+);\n', ahtml)
	if len(lst)!=0:
		lst1 = re.findall(r'("\d+":\s*[\s\S]*?),\s*"c', str(lst[0]).strip())
	else:
		lst1 =[]
	list_for_db = []
	url_list =[]
	for el in lst1:
		idCourse = int(re.findall(r'"(\d+)":\s*{', el)[0])
		nameCourse = re.findall(r'"title":\s*"([\s\S]*?)",\s*"', el)[0]
		urlCourse =url + re.findall(r'"url":\s*"/course/([\s\S]*?)"', el)[0]
		if searchWords.strip()=='*' or nameCourse.find(searchWords) != -1:
			list_for_db.append([idCourse, nameCourse, urlCourse])
	num_save = 0
	for el in list_for_db:
		if not Course.objects.filter(idCourse=el[0]).exists():
			instance = Course()
			instance.idCourse = el[0]
			instance.nameCourse = el[1]
			instance.urlCourse = el[2]
			instance.description = ''
			instance.nameUnivercity = ''
			try:
				instance.save()
				num_save = num_save + 1
			except Exception as e:
				print("Recording didn't save", e)
	print(list_for_db)
	return [len(list_for_db), num_save]



def get_courses_add(url):
    descriptionCourse = ''
    nameUnivercity = ''
    ahtml = get_html1(url)
    bs_str = bs(ahtml, 'html.parser')
    lst_div1 = bs_str.findAll('div', {'class':'description'}) # description of course
    lst_div2 = bs_str.findAll('a', {'class':'univercity-title'}) # name of univercity
    if len(lst_div1) !=0:
    	descriptionCourse = lst_div1[0].text
    if len(lst_div2) !=0:
    	nameUnivercity = lst_div2[0].text
    return [descriptionCourse, nameUnivercity]