import mysql.connector

class Database:
	mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root')
	def __init__(self):
		self.cursor = self.mydb.cursor(buffered = True)
		self.cursor.execute('CREATE DATABASE IF NOT EXISTS domain')
		self.cursor.execute('use domain')
		
	def add_whois(self,whois):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS whois(domain text,creation_date datetime, expiration_date datetime, registrar text,company text,raw mediumtext)')
		if type(whois['creation_date']) == list:
			whois['creation_date'] = whois['creation_date'][0]
		if type(whois['expiration_date']) == list:
			whois['expiration_date'] = whois['expiration_date'][0]
		if type(whois['company']) == list:
			whois['company'] = whois['company'][0]
		val = (whois['domain'],whois['creation_date'],whois['expiration_date'],whois['registrar'],whois['company'],whois['raw'])
		add = "INSERT INTO whois(domain, creation_date, expiration_date, registrar, company,raw) VALUES(%s,%s,%s,%s,%s,%s)"
		self.cursor.execute(add,val)
	
	def add_sub(self,sub):
		self.cursor.execute('CREATE TABLE IF NOT EXISTS subdomain(sub text,domain text)')
		val = (sub[1],sub[0])
		add = "INSERT INTO subdomain (sub,domain) VALUES(%s,%s)"
		self.cursor.execute(add,val)
		self.mydb.commit()
	
	def select_from_whois(self):
		try:
			self.cursor.execute('use domain')
			self.cursor.execute('SELECT * FROM whois')
			res = self.cursor.fetchall()
			return(res)
		except:
			return('')
		
	def select_from_subdomains(self):
		try:
			self.cursor.execute('use domain')
			self.cursor.execute('SELECT * FROM subdomain')
			res = self.cursor.fetchall()
			return(res)
		except:
			return('')
		
		











