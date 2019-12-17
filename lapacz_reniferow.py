from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def powiadomienie(x):
    fromaddr = ""
    toaddr = ""
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Python Bot | Zlapano renifera"
    body = "Zlapano renifera!!!\nIlosc zlapanych reniferow w obecnej sesji to: "+ str(x)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('1111', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("admin", "haslo")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
#Wywołanie przegladarki
browser = webdriver.Firefox()
#Wywolanie strony w przegladarce
browser.get('http://www.pepper.pl/login')
assert 'Zaloguj Się' in browser.title
nazwausera = ''
haslousera = ''
#Znalezienie pola do wpisania nazwy uzytkownika i hasla i wpisanie danych oraz symulacja wcisniecia klawisza enter
login = browser.find_element_by_xpath("//input[@id='login_form-identity']")
login.send_keys(nazwausera)
haslo = browser.find_element_by_xpath("//input[@id='login_form-password']")
haslo.send_keys(haslousera + Keys.RETURN)
#chwilowe wstrzymanie skryptu zeby strona sie wczytala
sleep(2)
#defnicja zmienniych uzytych w petli
#zmienna numerstrony przechowuje aktualny numer strony na ktorej przebywa uzytkownik
numerstrony = 0
#zmienna czasomierz przechowuje czas, przez ile sekund skrypt byl wstrzymywany w petli
czasomierz = 0
#zmienna zlapanerenifery przechowuje informacje o ilosci zlapanych reniferow
zlapanerenifery = 0

#Nieskonczona petla, musi byc manualnie przerwana. Do dopracowania w przyszłości.
while True:
	#próba znalezienia refniera
	try:
		#wyszukanie renifera po tagu html. Jezeli nie zostanie znaleziony to zostana wykonane polecenia znajdujace sie w bloku except
		renifer =  browser.find_element_by_xpath("//div[@data-handler='replace']")
		#klikniecie na renifera zeby go zebrac
		renifer.click()
		#zwiększenie zasobu złapanych reniferów
		zlapanerenifery += 1
		#wyświetlenie informacji o złapanym reniferze
		#generowanie timestampy
		ts = time.localtime()
		#print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
		print(time.strftime("%Y-%m-%d %H:%M:%S", ts) + '\tZnaleziono Renifera')
		powiadomienie(zlapanerenifery)
	#jeżeli renifer nie istnieje to zostanie wykonany kod z bloku except	
	except:
		#sprawdzenie czy czas jest równy 60 i jeżeli tak to:
		if czasomierz == 60:
			#zwiększamy numer strony o jeden
			numerstrony += 1
			#przechodzimy na kolejną stronę na której będziemy szukać refniera i scrollować w dół
			browser.get('http://www.pepper.pl/?page='+str(numerstrony))
		#jeżeli czasomierz jest większy od 60 to go zerujemy
		elif czasomierz >= 61:
			czasomierz = 0
		#sprawdzenie czy numer strony przekracza maksymalna ilosc stron istniejących na stronie pepper
		if numerstrony < 50:
			#Przewijanie strony w dół i opóźnianie działania skryptu
			browser.execute_script("window.scrollTo(0, 500)")
			sleep(0.5)
			browser.execute_script("window.scrollTo(0, 1000)")
			sleep(0.5)
			browser.execute_script("window.scrollTo(0, 1500)")
			sleep(0.5)
			browser.execute_script("window.scrollTo(0, 2000)")
			sleep(0.5)
			browser.execute_script("window.scrollTo(0, 5000)")
			sleep(3)
		else:
			#jeżeli numer strony przekracza limit, licznik zostaje wyzerowany i zaczynamy od początku
			numerstrony = 0
		#Dodanie wartości 5 za każdą iteracją. Jest to suma wszystkich sleepów wykoannych w powyższym bloku if
		czasomierz += 5		
		#wyświetlenie informacji o aktualnym czasie, numerze strony i ilości złapanych reniferów
		#generowanie timestampu
		ts = time.localtime()
		#print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
		print(time.strftime("%Y-%m-%d %H:%M:%S", ts) + '\tCzasomierz: ' + str(czasomierz)+'\tNumer Strony: '+str(numerstrony) + '\tRenifery: ' + str(zlapanerenifery))
		#powrót na początek pętli
		continue
