from bs4 import BeautifulSoup
import urllib2
import xlwt

#http://www.edulix.com/unisearch/univreview.php?univid=238   Indiana University-Bloomington
#http://www.edulix.com/unisearch/univreview.php?univid=206#  Georgia tech
#http://www.edulix.com/unisearch/univreview.php?univid=1222  University of Illinois Urbana-Champaign
#http://www.edulix.com/unisearch/univreview.php?univid=153   University of Southern California
#http://www.edulix.com/unisearch/univreview.php?univid=918   University of Texas Austin
#http://www.edulix.com/unisearch/univreview.php?univid=1510  Cornell University
#http://www.edulix.com/unisearch/univreview.php?univid=716   Carnegie Mellon University
#http://www.edulix.com/unisearch/univreview.php?univid=408   Northeastern University
#http://www.edulix.com/unisearch/univreview.php?univid=920   University of Texas Dallas
#http://www.edulix.com/unisearch/univreview.php?univid=142   University of California San Diego - 
#http://www.edulix.com/unisearch/univreview.php?univid=139   University of California Los Angeles - 
#http://www.edulix.com/unisearch/univreview.php?univid=812   University of Pennsylvania
#http://www.edulix.com/unisearch/univreview.php?univid=138   University of California Irvine - 
#http://www.edulix.com/unisearch/univreview.php?univid=1585  SUNY Buffalo
#http://www.edulix.com/unisearch/univreview.php?univid=1911  University of Wisconsin Madison - 
#http://www.edulix.com/unisearch/univreview.php?univid=570   North Carolina State University
#http://www.edulix.com/unisearch/univreview.php?univid=880   Texas A and M University College Station
#http://www.edulix.com/unisearch/univreview.php?univid=1410  University of Minnesota Twin Cities
#http://www.edulix.com/unisearch/univreview.php?univid=1127  University of Florida
#Ohio state university    647
#Rutgers University New Brunswick/Piscataway
#Purdue University    252

#CHANGE::write the URL and the name you want to give to the file
dictionary = {'http://www.edulix.com/unisearch/univreview.php?univid=1301':'Johns Hopkins University-accept'
              }

for key in dictionary:
    data = urllib2.urlopen(key).read()
    soup = BeautifulSoup(data, 'html.parser')
    
    #CHANGE::choose from the 2 options, either admit or reject
    mydivs = soup.findAll("a", { "class" : "admit" })
    #mydivs = soup.findAll("a", { "class" : "reject" })
    
    universityName = dictionary[key]
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    
    list = []
    
    for x in mydivs:
        list.append(x['href'])
    
    print 'staring to parse'
    print len(list)
    j = 1;
    for x in list:
    #    if j >= 286:
        try:
            newPageData = urllib2.urlopen("http://www.edulix.com/unisearch/" + x).read()
            soup = BeautifulSoup(newPageData, 'html.parser')
            
            quantScore = 0
            verbalScore = 0
            total = 0
            awaScore = ''
            toeflScore = ''
            major = ''
            term = ''
            specialization = ''
            college = ''
            department = ''
            grade = ''
            publications = ''
            experience = ''
            details = ''
            
            # this gives the quant score
            if soup.find(id="page").find('table').find(text = 'Quantitative:'):
                if soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.contents[5]:
                    quantScore = soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.contents[5].contents[0].strip()
                # this gives the verbal score
                if soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.contents[9]:
                    verbalScore = soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.contents[9].contents[0].strip()
                total = int(quantScore) + int(verbalScore)
                # AWA
                if soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.contents[13]:
                    awaScore = soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.contents[13].contents[0].strip()
                # TOEFL
                if soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.parent.find(text='TOEFL').parent.parent.contents[5]:
                    toeflScore = soup.find(id="page").find('table').find(text = 'Quantitative:').parent.parent.parent.find(text='TOEFL').parent.parent.contents[5].contents[0].strip()
            #major
            if soup.find(id="page").find('table').find(text = 'Major'):
                major = soup.find(id="page").find('table').find(text = 'Major').parent.parent.contents[3].contents[0].strip()
            #Term and Year
            if soup.find(id="page").find('table').find(text = 'Term and Year'):
                term = soup.find(id="page").find('table').find(text = 'Term and Year').parent.parent.contents[3].contents[0].strip()
            #Specialization
            if soup.find(id="page").find('table').find(text = 'Specialization'):
                specialization = soup.find(id="page").find('table').find(text = 'Specialization').parent.parent.contents[3].contents[0].strip()
            #University/College
            if soup.find(id="page").find('table').find(text = 'University/College'):
                college = soup.find(id="page").find('table').find(text = 'University/College').parent.parent.contents[3].contents[0].strip()
            #Department
            if soup.find(id="page").find('table').find(text = 'Department'):
                department = soup.find(id="page").find('table').find(text = 'Department').parent.parent.contents[3].contents[0].strip()
            #Grade
            if soup.find(id="page").find('table').find(text = 'Grade'):
                grade = soup.find(id="page").find('table').find(text = 'Grade').parent.parent.contents[3].contents[0].strip()
            #Journal Publications
            if soup.find(id="page").find('table').find(text = 'Journal Publications'):
                publications = soup.find(id="page").find('table').find(text = 'Journal Publications').parent.parent.contents[3].contents[0].strip()
            #Industrial Experience
            if soup.find(id="page").find('table').find(text = 'Industrial Experience'):
                experience = soup.find(id="page").find('table').find(text = 'Industrial Experience').parent.parent.contents[3].contents[0].strip()
            #Other Miscellaneous Details
            if soup.find(id="page").find('table').find(text = 'Other Miscellaneous Details'):
                details = soup.find(id="page").find('table').find(text = 'Other Miscellaneous Details').parent.parent.find_next_sibling('tr').contents[1].get_text().strip()
            
            temp = soup.find(id="page").find_all('table')[2].find_all('tr')[1:]
            i = 0;
        #    print 'temp :: ' 
        #    print  temp
            
            finalStr = []
            while i < len(temp):
        #        print 'temp[i] :: ' 
        #        print temp[i]
                university = temp[i].find_all('td')[0].find('a').get_text()
                acceptance = temp[i].find_all('td')[1].find('span').get_text()
                i = i + 1
                if(i < len(temp)):
                    if temp[i].find_all('td')[0].find('a'):
                        about = ''
                    else:
                        about = temp[i].find('td').get_text()
                        finalStr.append(university + " " + acceptance + " \n" + about + " \n")
                        i = i + 1
                else:
                    about = ''
                
            ws.write(j, 0, quantScore)
            ws.write(j, 1, verbalScore)
            ws.write(j, 2, total)
            ws.write(j, 3, awaScore)
            ws.write(j, 4, toeflScore)
            ws.write(j, 5, major)
            ws.write(j, 6, term)
            ws.write(j, 7, specialization)
            ws.write(j, 8, college)
            ws.write(j, 9, department)
            ws.write(j, 10, grade)
            ws.write(j, 11, publications)
            ws.write(j, 12, experience)
            ws.write(j, 13, details)
            ws.write(j, 14, finalStr)
            #CHANGE::you might want to change the location for saving the file
            wb.save("/Users/rd22/Documents/edulix_"+ universityName +".xls")
            j+=1
        except Exception:
            print 'quantScore: ' + quantScore + 'verbalScore: ' + verbalScore + 'awaScore: ' + awaScore + 'toeflScore: ' + toeflScore + ' ' + major + ' ' + term + ' ' + specialization + ' ' + college + ' ' + department + ' ' + grade + ' ' + publications + ' ' + experience + ' ' + details
            print finalStr  
    print 'done one'

print 'end...'
    
