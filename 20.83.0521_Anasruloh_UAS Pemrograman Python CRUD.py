import requests
import mysql.connector

mydb = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password="",
	database="db_akademik_0521"
	)

if mydb.is_connected():
	print("Sukses !")

def write_db_api():
	newdict={ }
	url = 'https://api.abcfdab.cfd/students'
	response = requests.get(url)
	data = response.json()
	cursor = mydb.cursor()
	sql = '''INSERT INTO tbl_students_0521(id,nim,nama,jk,jurusan,alamat) VALUES (%s,%s,%s,%s,%s,%s) '''

	for i in data['data']:
		print(i)
		print(type(i))
		val = (i['id'], i['nim'], i['nama'], i['jk'], i['jurusan'], i['alamat'])
		cursor.execute(sql,val)
		mydb.commit()

def tampil_data():
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM tbl_students_0521")
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def tampil_limit():
	baris = input("\nBerapa limitnya yang di tampilkan : ")
	mycursor = mydb.cursor()
	sql = ("SELECT * FROM tbl_students_0521")
	mycursor.execute(sql + baris)
	myresult = mycursor.fetchmany(baris)
	for x in myresulst:
		print(x)

def tampilkan_nim():
	petik = "'"
	nim = input('Masukan NIM :')
	mycursor = mydb.cursor()
	sql = ("SELECT * FROM 'tbl_students_0521' WHERE nim=" )
	mycursor.execute(sql + petik + nim + nim )
	myresult = mycursor.fethone()
	print(myresult)

if __name__ == '__main__':
	write_db_api()

	while True:
		print("\n_________________API PROGRAM______________\n")
		print("1. Tampilkan seluruh data")
		print("2. Tampilkan data limit")
		print("3. Tampilkan data dari NIM")
		print("4. Keluar\n")
		menu = int(input("Masukan Pilihan Menu : "))
		if menu == 1 :
			tampil_data()
		if menu == 2 :
			tampil_limit()
		if menu == 3:
			tampilkan_nim()
		if menu == 4:
			break
		else :
			print('YANG ADA MASUKAN SALAH!!!')