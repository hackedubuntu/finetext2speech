import requests
import os
import sys

class ConvertText(object):
	"""docstring for ConvertText"""
	def __init__(self):
		super(ConvertText, self).__init__()
		self.enc = ""
		self.text = ""
		self.lang = ""
		self.speed = ""
		self.url = ""
		self.filename = ""
		self.yildizlar = "*"*10
		self.languages = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn',
						'bs', 'bg', 'ca', 'ceb', 'ny', 'co', 'hr',
						'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy',
						'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'he', 'hi',
						'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn',
						'kk', 'km', 'ko', 'ku', 'ky', 'lao', 'lo', 'la', 'lv', 'lt',
						'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my',
						'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru',
						'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so',
						'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk',
						'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
		
	def set_encoding(self):
		try:
			self.enc = input(f"{self.yildizlar} - Type encoding(e.q.: UTF-8,ANSI,Windows-1254,ASCII): ")
			if self.enc in ["UTF-8","ANSI","Windows-1254","ASCII"]:
				return self.enc
			else:
				return "UTF-8"
		except KeyboardInterrupt:
			exit()
		except:
			print()
			self.set_encoding()

	def set_text(self):
		try:
			self.text = input(f"{self.yildizlar} - Type what you want to convert text to speech: ")
			if self.text:
				return self.text
			else:
				return "Hello World"
		except KeyboardInterrupt:
			exit()
		except:
			print()
			self.set_text()

	def set_lang(self):
		try:
			self.lang = input(f"{self.yildizlar} - Type lang(such as 'en' or 'tr')             : ")
			if self.lang in self.languages:
				return self.lang
			else:
				return "en"
		except KeyboardInterrupt:
			exit()
		except:
			print()
			self.set_lang()

	def set_speed(self):
		try:
			self.speed = float(input("********** - Set speed of voice (between 0.1 - 1.0) : "))
			print("1")
			if self.speed > 0.0 and self.speed < 1.0:
				print("2")
				return str(self.speed)
			else:
				print("3")
				return "0.8"
		except KeyboardInterrupt:
			print("4")
			exit()
		except Exception as e:
			print("5")
			print(e)
			self.set_speed()

	def isitafile(self):
		try:
			isit = input(f"{self.yildizlar} - Is there a file I should take care of ? y/n: ").strip()
			if isit.lower() == "y":
				texts = []
				wherethefile = input(f"{self.yildizlar} - Where is the file: ").strip()
				with open(wherethefile,"r",encoding="utf8") as f:
					texts = [str(x).strip() for x in f.readlines()]
				return (True,texts)
			elif isit.lower() == "n":
				return (False,[])
		except KeyboardInterrupt:
			exit()
		except:
			self.isitafile()


	def downloadVoice(self):
		self.fileornot = self.isitafile()
		if self.fileornot[0]:
			self.enc = self.set_encoding()
			self.text = self.fileornot[1]
			self.lang = self.set_lang()
			self.speed = self.set_speed()
			self.filename = "_".join(x for x in self.text[0].strip().split())
			if len(self.filename) > 35:
				self.filename = self.filename[:35] + ".mp3"
			else:
				self.filename = self.filename + ".mp3"
			

			total_len = len(self.text)
			with open(self.filename,"wb") as f:
				for x in range(len(self.text)):
					self.url = f"""https://translate.google.com/translate_tts?ie={self.enc}&q={self.text[x]}&tl={self.lang}&ttsspeed={self.speed}&total=1&idx=1&client=tw-ob&textlen={len(self.text[x])}"""
					r = requests.get(self.url,stream=True)
					f.write(r.content)
					print(f"\r{self.yildizlar} - % {int((x/total_len)*100)} of file is converted into audio in {self.filename} !!!",end="")
			print("\nIt is done!!!")
		elif self.fileornot[0] == False:
			self.enc = self.set_encoding()
			self.text = self.set_text()
			self.lang = self.set_lang()
			self.speed = self.set_speed()
			texto = self.text.split()
			self.filename = texto[0] + ".mp3"
			self.url = f"""https://translate.google.com/translate_tts?ie={self.enc}&q={self.text}&tl={self.lang}&ttsspeed={self.speed}&total=1&idx=1&client=tw-ob&textlen={len(self.text)}"""

			r = requests.get(self.url,stream=True)
			with open(self.filename,"wb") as f:
				f.write(r.content)
			print(f"{self.yildizlar} - It is done in {self.filename} !!!")
try:
	ct = ConvertText()
	ct.downloadVoice()
except Exception as e:
	print(e)