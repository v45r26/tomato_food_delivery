import eel
import time
import random as rd
import mysql.connector as mysql


# Function Adda

# Import time module before using this
# Sleep function for 1 sec use slp(1)
def slp(val): 
	time.sleep(val)

# Login [ START ]
@eel.expose
def login(data):
	sp_data = data.split('|')
	un = sp_data[0]
	ps = sp_data[1]

	# print('UNAME : ',un)
	# print('PASS  : ',ps)

	cred_check = log_fn(un,ps)

	return cred_check
# Login [ END ]

# SIGNUP [ START ]
@eel.expose
def signup(data):
	sp_data = data.split('|')
	na = sp_data[0]
	un = sp_data[1]
	em = sp_data[2]
	ps = sp_data[3]
	cp = sp_data[4]

	# print('NAME  : ',na)
	# print('UNAME : ',un)
	# print('EMAIL : ',em)
	# print('PASS  : ',ps)
	# print('CPASS : ',cp)

	upld_cred = sign_up_fn(na,un,em,ps)
	return upld_cred
# SIGNUP [ STOP ] 

# default Value
db_pass = 'root'
db_name = 'tomato_food_delievery'

# Printing 
print('__________ TOMATO FOOD DELIEVERY __________')
print()
slp(1)
print('>>> Connecting to MySQL Server...')

# connecting to MySql
sc_mq = mysql.connect(
					host='localhost',
					user='root',
					password=db_pass,
					auth_plugin='mysql_native_password')
if sc_mq.is_connected():
	print('----- Connected!')
else:
	print('----- Unable to Connect!')

sc_mq_cur = sc_mq.cursor() # partial curcur
sc_mq_cur.execute('show databases')
slp(1)
print()
print('>>> Let\'s check Database Exist or Not...')

# for collecting database list
db_cont = []

for x in sc_mq_cur:
	db_cont.append(x[0])

# print(db_cont)
slp(1)
if db_name in db_cont:
	print('----- Requirement Already Satisfied!')
else:
 	print('----- Creating Database!')
 	sc_mq_cur.execute(f'CREATE DATABASE `{db_name}`')
 	# conn.commit()

# closing whole database
sc_mq.close()

print()
print('>>> Connecting to MySQL Database!')
# Let's connect to user database server
conn = mysql.connect(
					host='localhost',
					user='root',
					password=db_pass,
					database=db_name,
					auth_plugin='mysql_native_password'
					)

if conn.is_connected():
	print('----- Connected!')
else:
	print('----- Unable to Connect!')

cur = conn.cursor()
slp(1)
# Creating user table
print()
print('>>> Creating user Table')
utc_query = '''
			CREATE TABLE IF NOT EXISTS user_t(
			sno integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
			name text NOT NULL,
			u_name varchar(100) NOT NULL,
			u_password varchar(100) NOT NULL,
			u_email varchar(100) NOT NULL
			)

'''
cur.execute(utc_query)
conn.commit()
slp(1)
print('----- Created Successfully!')
# Creating food menu table
slp(1)
print()
print('>>> Creating Food Menu Table')
ftc_query = '''
			CREATE TABLE IF NOT EXISTS food_m(
			sno integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
			f_id varchar(20) NOT NULL,
			f_name text NOT NULL,
			f_cat text NOT NULL,
			f_img text NOT NULL,
			f_price int NOT NULL
			)

'''
cur.execute(ftc_query)
conn.commit()
slp(1)
print('----- Created Successfully!')
# Creating Order table
slp(1)
print()
print('>>> Creating Order Table')
otc_query = '''
			CREATE TABLE IF NOT EXISTS order_t(
			sno integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
			o_id text NOT NULL,
			f_id text NOT NULL,
			u_id text NOT NULL,
			o_otp int NOT NULL,
			o_status text NOT NULL
			)

'''
cur.execute(otc_query)
conn.commit()
slp(1)
print('----- Created Successfully!')
slp(1)

# Function for uploading data first check data exist or not
print()
print('>>> Uploading Food Menu')
slp(1)
cur.execute("SELECT * FROM food_m")
fd_d = cur.fetchall()
fd_count = cur.rowcount
# print('menu = ',fd_count)
# slp(1)
if fd_count  > 0:
	print('----- Requirement Already Satisfied!')
else:
	print('----- Uploading Data')
	f_ins_dat = """
	INSERT INTO food_m(sno,f_id,f_name,f_cat,f_img,f_price) VALUES
	(NULL,'tmt_fd_pizza_001','Pepperoni Pizza','pizza veg','pizza_001.png',250),
	(NULL,'tmt_fd_soup_001','Tomato Soup','soup veg','soup_001.png',40),
	(NULL,'tmt_fd_burger_001','Cheese Burger','burger','burger_001.png',85),
	(NULL,'tmt_fd_rolls_001','Veg Roll','rolls veg','rolls_001.png',20),
	(NULL,'tmt_fd_dosa_001','Cheese Dosa','dosa veg','dosa_001.png',75),
	(NULL,'tmt_fd_indian_001','Litti Chokha','indian veg','indian_001.png',20),
	(NULL,'tmt_fd_pizza_002','Red Chilli Pizza','pizza veg','pizza_002.png',200),
	(NULL,'tmt_fd_soup_002','Mashroom Soup','soup veg','soup_002.png',80),
	(NULL,'tmt_fd_burger_002','Egg Burger','burger nonvg','burger_002.png',45),
	(NULL,'tmt_fd_rolls_002','Egg Roll','rolls nonvg','rolls_002.png',25),
	(NULL,'tmt_fd_dosa_002','Masala Dosa','dosa veg','dosa_002.png',50),
	(NULL,'tmt_fd_indian_002','Jalebi','indian veg','indian_002.png',100),
	(NULL,'tmt_fd_pizza_003','Chicken Pizza','pizza nonvg','pizza_003.png',300),
	(NULL,'tmt_fd_soup_003','Sweet Corn','soup veg','soup_003.png',50),
	(NULL,'tmt_fd_burger_003','Chicken Burger','burger nonvg','burger_003.png',90),
	(NULL,'tmt_fd_rolls_003','Chicken Roll','rolls nonvg','rolls_003.png',50),
	(NULL,'tmt_fd_dosa_003','Moong Dal Dosa','dosa veg','dosa_003.png',120),
	(NULL,'tmt_fd_indian_003','Poha','indian veg','indian_003.png',60),
	(NULL,'tmt_fd_pizza_004','Paneer Pizza','pizza veg','pizza_004.png',250),
	(NULL,'tmt_fd_soup_004','Spinach Corn Soup','soup veg','soup_004.png',60),
	(NULL,'tmt_fd_burger_004','Paneer Burger','burger','burger_004.png',60),
	(NULL,'tmt_fd_rolls_004','Mutton Roll','rolls nonvg','rolls_004.png',50),
	(NULL,'tmt_fd_dosa_004','Paneer Dosa','dosa veg','dosa_004.png',150),
	(NULL,'tmt_fd_indian_004','Chilli Paneer','indian veg','indian_004.png',150),
	(NULL,'tmt_fd_pizza_005','Margherita Pizza','pizza veg','pizza_005.png',400),
	(NULL,'tmt_fd_soup_005','Spring Onion Soup','soup veg','soup_005.png',100),
	(NULL,'tmt_fd_burger_005','Veg Burger','burger','burger_005.png',30),
	(NULL,'tmt_fd_rolls_005','Spring Roll','rolls veg','rolls_005.png',65),
	(NULL,'tmt_fd_dosa_005','Mysore Masala Dosa','dosa veg','dosa_005.png',140),
	(NULL,'tmt_fd_indian_005','Dal Makhani','indian veg','indian_005.png',80),
	(NULL,'tmt_fd_pizza_006','Onion Pizza','pizza veg','pizza_006.png',150),
	(NULL,'tmt_fd_soup_006','Manchow Soup','soup veg','soup_006.png',60),
	(NULL,'tmt_fd_burger_006','Bacon Burger','burger','burger_006.png',85),
	(NULL,'tmt_fd_dosa_006','Paneer Chilli Dosa','dosa veg','dosa_006.png',160),
	(NULL,'tmt_fd_indian_006','Rashgulla','indian veg','indian_006.png',200)	
	"""
	cur.execute(f_ins_dat)
	conn.commit()
	print('----- Uploaded Successfully!')
print()
slp(1)

# Signup Function
def sign_up_fn(name,u_name,email,password):
	print('>>> Uploading Credential!')
	cur.execute(f"INSERT INTO user_t(sno,name,u_name,u_password,u_email) VALUES(NULL,'{name}','{u_name}','{password}','{email}')")
	conn.commit()

	data = log_fn(u_name,password)
	return data

# Login Function
def log_fn(u_name,password):
	print('>>> Checking Credential!')
	cur.execute(f"SELECT * FROM user_t WHERE u_name = '{u_name}' AND u_password = '{password}'")
	data = cur.fetchall()
	count = cur.rowcount
	# print(data,'  ___   ',count)
	if count == 1:
		print('----- Success')
		return 'success'
	else:
		print('----- Something Went Wrong!')
		return 'Something Went Wrong!'

# get user data
@eel.expose
def get_user_data_b_py(u_name):
	cur.execute(f"SELECT * FROM user_t WHERE u_name = '{u_name}'")
	data = cur.fetchone()
	cnt = cur.rowcount
	if cnt == 1:
		name = data[1]
		# data[2]
		# data[3]
		# data[4]
		return name
	else:
		return 'Something Went Wrong!'


@eel.expose
def get_fd_data_b_py(uid):
	cur.execute("SELECT * FROM food_m")
	fd_data = cur.fetchall()
	ret_dat_b = ''
	for fd in fd_data:
		# x[1] Food ID
		# x[2]  Name
		# x[3] catogery
		# x[4] img add
		# x[5] price
		ret_dat_b += f'''
		<div class=\"column {fd[3]}\">
    		<div class=\"content\">
    			<img src=\"../assets/fd_images/{fd[4]}\" alt=\"Car\" class=\"img_d\">
      			<div class=\"dis_prc\">$ {fd[5]}</div>
      			<div class=\"dis_na\">{fd[2]}</div>
      			<button class=\"odr_btn_c\" onclick=\"set_order(\'{uid}\',\'{fd[1]}\')\">Buy</button>
    		</div>
		</div>	
		'''
	return ret_dat_b

# Order
@eel.expose
def set_order_py(uid,f_id):
	otp = ''

	for x in range(6):
		otp += str(rd.randrange(0,9))
	
	order_id = 'tfd_oid_'+otp # ORDER ID
	fotp = int(otp) # OTP
	# print(order_id)
	# print(f_id)
	# print(uid)
	# print(fotp)

	cur.execute(f"INSERT INTO order_t(sno,o_id,f_id,u_id,o_otp,o_status) VALUES(NULL,'{order_id}','{f_id}','{uid}','{fotp}','ordered')")
	conn.commit()


# Display myOrder
@eel.expose
def get_myorder_f_py(uid):
	cur.execute(f"SELECT * FROM order_t WHERE u_id = '{uid}' ORDER BY sno DESC")
	or_m = cur.fetchall()
	ret_or_m = ''
	for dat in or_m:
		# dat[1] order i]d
		# dat[2] food id
		# dat[4] otp
		cur.execute(f"SELECT * FROM food_m WHERE f_id = '{dat[2]}'")
		fd_da = cur.fetchone()
		# fd_da[2] food name
		# fd_da[4] img
		# fd_da[5] price

		if dat[5] == 'can':
			ret_or_m += f'''
				<div class="or_d_b">
					<div class="img_di">
						<img src="../assets/fd_images/{fd_da[4]}">
					</div>
					<div class="dst_d">
						<div class="nam_d">
							<span>{fd_da[2]}</span>
							<span class="rec_d">CANLCELED</span>
						</div>
						<div class="pric_d">$ {fd_da[5]}</div>
						<div class="btn_d_or">
							<div class="otp">OTP - {dat[4]}</div>
							<button onclick="can_or('{dat[1]}')" disabled>Cancel</button>
							<button onclick="res_or('{dat[1]}')" disabled>Recieved</button>
						</div>
					</div>
				</div>'''

		if dat[5] == 'rec':
			ret_or_m += f'''
				<div class="or_d_b">
					<div class="img_di">
						<img src="../assets/fd_images/{fd_da[4]}">
					</div>
					<div class="dst_d">
						<div class="nam_d">
							<span>{fd_da[2]}</span>
							<span class="can_d">RECIEVED</span>
						</div>
						<div class="pric_d">$ {fd_da[5]}</div>
						<div class="btn_d_or">
							<div class="otp">OTP - {dat[4]}</div>
							<button onclick="can_or('{dat[1]}')" disabled>Cancel</button>
							<button onclick="res_or('{dat[1]}')" disabled>Recieved</button>
						</div>
					</div>
				</div>'''

		if dat[5] == 'ordered':
			ret_or_m += f'''
				<div class="or_d_b">
					<div class="img_di">
						<img src="../assets/fd_images/{fd_da[4]}">
					</div>
					<div class="dst_d">
						<div class="nam_d">
							<span>{fd_da[2]}</span>
							<span></span>
						</div>
						<div class="pric_d">$ {fd_da[5]}</div>
						<div class="btn_d_or">
							<div class="otp">OTP - {dat[4]}</div>
							<button onclick="can_or('{dat[1]}')">Cancel</button>
							<button onclick="res_or('{dat[1]}')">Recieved</button>
						</div>
					</div>
				</div>'''
	return ret_or_m

# Cancel order
@eel.expose
def can_order_py(oid):
	cur.execute(f"UPDATE order_t SET o_status = 'can' WHERE o_id = '{oid}'")
	conn.commit()

# Recieve order
@eel.expose
def rec_order_py(oid):
	cur.execute(f"UPDATE order_t SET o_status = 'rec' WHERE o_id = '{oid}'")
	conn.commit()

# START Displaying UI
print('>>> EEL Server is Starting Now...')
print()
eel.init('ui')
eel.start('index.html')
# eel.start('tab/index.html?un=_berlin')

# ____COMPLEATED____