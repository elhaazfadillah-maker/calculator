import tkinter as tk


layar_utama = tk.Tk()
layar_utama.title("kalkulator")
layar_utama.geometry("350x500")
layar_utama.configure(bg="#202021")

papan_hitung = ""

 
def tekan_tombol(num):
  global papan_hitung
  papan_hitung = papan_hitung + str(num)
  string_tampilan.set(papan_hitung)
def hitung():
  global papan_hitung
  try:
    total = str(eval(papan_hitung.replace('x', '*').replace('÷', '/').replace(',','.')))
    string_tampilan.set(total)
    papan_hitung = total
  except:
    string_tampilan.set("error")
    papan_hitung = ""    
def hapus_semua():
  global papan_hitung
  papan_hitung = ""
  string_tampilan.set("")
                      
string_tampilan = tk.StringVar()

layar = tk.Entry(
  layar_utama,  
  textvariable=string_tampilan,  
  font=("Helvetica", 36), 
  bd=0, 
  bg="#fafefa", 
  fg="black", 
  justify="right"
)
layar.pack(fill="both", ipadx=10, ipady=30, padx=10, pady=10)

frame_tombol = tk.Frame(layar_utama, bg="#f6fbf7") 
frame_tombol.pack(fill="both", expand=True, padx=10, pady=10)

for i in range(5):
  frame_tombol.rowconfigure(i, weight=1)
for i in range(4):
  frame_tombol.columnconfigure(i, weight=1)

tombol_config = [
  ('C', 0, 0, '#a5a5a5', 'black', hapus_semua),
  ('+/-', 0, 1, '#a5a5a5', 'black', lambda: tekan_tombol('-')),
  ('%', 0, 2, '#a5a5a5', 'black', lambda: tekan_tombol('/100')),
  ('÷', 0, 3, "#2B00FF", 'white', lambda: tekan_tombol('÷')),
    
  ('1', 1, 0, '#333333', 'white', lambda: tekan_tombol('1')),
  ('2', 1, 1, '#333333', 'white', lambda: tekan_tombol('2')),
  ('3', 1, 2, '#333333', 'white', lambda: tekan_tombol('3')),
  ('x', 1, 3, "#4b0aff", 'white', lambda: tekan_tombol('x')),
    
  ('4', 2, 0, '#333333', 'white', lambda: tekan_tombol('4')),
  ('5', 2, 1, '#333333', 'white', lambda: tekan_tombol('5')),
  ('6', 2, 2, '#333333', 'white', lambda: tekan_tombol('6')),
  ('-', 2, 3, "#2f0aff", 'white', lambda: tekan_tombol('-')),
    
  ('7', 3, 0, '#333333', 'white', lambda: tekan_tombol('7')),
  ('8', 3, 1, '#333333', 'white', lambda: tekan_tombol('8')),
  ('9', 3, 2, '#333333', 'white', lambda: tekan_tombol('9')),
  ('+', 3, 3, "#0a16ff", 'white', lambda: tekan_tombol('+')),
    
  (',', 4, 2, '#333333', 'white', lambda: tekan_tombol(',')),
  ('=', 4, 3, "#1e0aff", 'white', hitung)
]

for teks, r, c, bg_color, fg_color, aksi in tombol_config:
  btn = tk.Button(
    frame_tombol, text=teks, font=("Helvetica", 18, "bold"),
    bg=bg_color, fg=fg_color, bd=0, relief="flat", command=aksi
  )
  btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
  btn_nol = tk.Button(
  frame_tombol, text="0", font=("Helvetica", 18, "bold"),
  bg="#333333", fg="white", bd=0, relief="flat", command=lambda: tekan_tombol('0')
 )
btn_nol.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

layar_utama.mainloop()
