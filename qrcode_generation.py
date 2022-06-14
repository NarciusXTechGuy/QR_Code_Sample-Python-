#Author:-NarciuxTechGuy
#14/06/2022
#
#"pip install qrcode" this command should be initialized before writing the code.\\
#
import qrcode
#
qr_code_url='Link/messages_ahown_in_qr_code' #The value which shows after scanning should be given here for eg: "sample_massage_which_the_value_is_shown"
print("qr")
qr_code_input=str(qr_code_url)
# print(qr_code_input)
img = qrcode.make(qr_code_input)
sample_name="name_of_the_file" #The name of the file must be given here
qr_code_name=sample_name+".png"
qr_code=img.save(qr_code_name)
print(qr_code_name)
 #  
#After writing the code run "python name_of_file.py" Command in the Terminal
