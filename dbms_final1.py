import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ================== DB CONNECTION ==================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="woobbyY@111",   # change if needed
        database="railway_system"
    )

# ================== PASSENGER ==================
def add_passenger_window():
    win = tk.Toplevel(root)
    win.title("Add Passenger")

    labels = ["First Name", "Middle Name", "Last Name",
              "Phone Number", "Gender", "Age", "Address"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_passenger():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO PASSENGER (fname, mname, lname, phone_number, gender, age, address)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(q, (
                entries["First Name"].get(),
                entries["Middle Name"].get() or None,
                entries["Last Name"].get(),
                entries["Phone Number"].get(),
                entries["Gender"].get(),
                entries["Age"].get() or None,
                entries["Address"].get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Passenger added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_passenger).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_passengers_window():
    win = tk.Toplevel(root)
    win.title("Passenger List")
    win.geometry("800x400")

    cols = ("ID", "First Name", "Middle Name", "Last Name",
            "Phone", "Gender", "Age", "Address")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=90)

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, fname, mname, lname, phone_number, gender, age, address FROM PASSENGER")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== TRAIN ==================
def add_train_window():
    win = tk.Toplevel(root)
    win.title("Add Train")

    labels = ["Train Name", "Reservation", "Compartment Chart", "Station"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_train():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO TRAIN_DETAILS (train_name, reservation, compartment_chart, station)
                VALUES (%s,%s,%s,%s)
            """
            cur.execute(q, (
                entries["Train Name"].get(),
                entries["Reservation"].get(),
                entries["Compartment Chart"].get(),
                entries["Station"].get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Train added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_train).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_trains_window():
    win = tk.Toplevel(root)
    win.title("Train List")
    win.geometry("700x400")

    cols = ("Train No", "Train Name", "Reservation", "Compartment Chart", "Station")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=120)

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT train_number, train_name, reservation, compartment_chart, station FROM TRAIN_DETAILS")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== SUPERVISOR ==================
def add_supervisor_window():
    win = tk.Toplevel(root)
    win.title("Add Technical Supervisor")

    labels = ["First Name", "Middle Name", "Last Name", "Phone Number", "Email"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_supervisor():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO TECHNICAL_SUPERVISOR (fname, mname, lname, phone_number, email)
                VALUES (%s,%s,%s,%s,%s)
            """
            cur.execute(q, (
                entries["First Name"].get(),
                entries["Middle Name"].get() or None,
                entries["Last Name"].get(),
                entries["Phone Number"].get(),
                entries["Email"].get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Supervisor added successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_supervisor).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_supervisors_window():
    win = tk.Toplevel(root)
    win.title("Supervisors")
    win.geometry("750x400")

    cols = ("ID", "First Name", "Middle Name", "Last Name", "Phone", "Email")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=110)

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT supervisor_id, fname, mname, lname, phone_number, email FROM TECHNICAL_SUPERVISOR")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== TICKET ==================
def issue_ticket_window():
    win = tk.Toplevel(root)
    win.title("Issue Ticket")

    labels = ["Passenger ID", "Destination", "Date (YYYY-MM-DD)",
              "Time (HH:MM:SS)", "Reservation Class",
              "Train Number", "Extra Train Details"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_ticket():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO TICKET
                (passenger_id, destination, date_of_journey, time_of_journey,
                 reservation, train_number, train_details)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(q, (
                entries["Passenger ID"].get(),
                entries["Destination"].get(),
                entries["Date (YYYY-MM-DD)"].get(),
                entries["Time (HH:MM:SS)"].get() or None,
                entries["Reservation Class"].get(),
                entries["Train Number"].get() or None,
                entries["Extra Train Details"].get() or None
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Ticket issued successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_ticket).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_tickets_window():
    win = tk.Toplevel(root)
    win.title("Tickets")
    win.geometry("1000x400")

    cols = ("Ticket ID", "Passenger", "Destination", "Date",
            "Time", "Class", "Train No", "Train Name")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=110)

    try:
        conn = get_connection()
        cur = conn.cursor()
        q = """
            SELECT
                T.ticket_id,
                CONCAT(P.fname,' ',P.lname) AS passenger_name,
                T.destination,
                T.date_of_journey,
                T.time_of_journey,
                T.reservation,
                T.train_number,
                TD.train_name
            FROM TICKET T
            JOIN PASSENGER P ON T.passenger_id = P.id
            LEFT JOIN TRAIN_DETAILS TD ON T.train_number = TD.train_number
        """
        cur.execute(q)
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== PAYMENT ==================
def record_payment_window():
    win = tk.Toplevel(root)
    win.title("Record Payment")

    labels = ["Passenger ID", "Ticket ID", "Total Payment",
              "Payment Date (YYYY-MM-DD)", "Payment Mode"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_payment():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO PAYMENT
                (passenger_id, ticket_id, total_payment, payment_date, payment_mode)
                VALUES (%s,%s,%s,%s,%s)
            """
            cur.execute(q, (
                entries["Passenger ID"].get(),
                entries["Ticket ID"].get(),
                entries["Total Payment"].get(),
                entries["Payment Date (YYYY-MM-DD)"].get(),
                entries["Payment Mode"].get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Payment recorded successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_payment).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_payments_window():
    win = tk.Toplevel(root)
    win.title("Payments")
    win.geometry("900x400")

    cols = ("Payment ID", "Passenger", "Ticket ID",
            "Amount", "Date", "Mode")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=120)

    try:
        conn = get_connection()
        cur = conn.cursor()
        q = """
            SELECT
                PY.payment_id,
                CONCAT(P.fname,' ',P.lname) AS passenger_name,
                PY.ticket_id,
                PY.total_payment,
                PY.payment_date,
                PY.payment_mode
            FROM PAYMENT PY
            JOIN PASSENGER P ON PY.passenger_id = P.id
        """
        cur.execute(q)
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== CHECKS ==================
def record_check_window():
    win = tk.Toplevel(root)
    win.title("Record Check (Passenger–Train)")

    labels = ["Passenger ID", "Train Number", "Check Date (YYYY-MM-DD)"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_check():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO CHECKS (passenger_id, train_number, check_date)
                VALUES (%s,%s,%s)
            """
            cur.execute(q, (
                entries["Passenger ID"].get(),
                entries["Train Number"].get(),
                entries["Check Date (YYYY-MM-DD)"].get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Check recorded successfully!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_check).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_checks_window():
    win = tk.Toplevel(root)
    win.title("Checks (Passenger–Train)")
    win.geometry("900x400")

    cols = ("Passenger", "Train No", "Train Name", "Check Date")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=150)

    try:
        conn = get_connection()
        cur = conn.cursor()
        q = """
            SELECT
                CONCAT(P.fname,' ',P.lname) AS passenger_name,
                C.train_number,
                TD.train_name,
                C.check_date
            FROM CHECKS C
            JOIN PASSENGER P ON C.passenger_id = P.id
            JOIN TRAIN_DETAILS TD ON C.train_number = TD.train_number
        """
        cur.execute(q)
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== MANAGE (SUPERVISOR–TRAIN) ==================
def assign_manage_window():
    win = tk.Toplevel(root)
    win.title("Assign Supervisor to Train")

    labels = ["Supervisor ID", "Train Number"]
    entries = {}
    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
        ent = tk.Entry(win, width=30)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries[text] = ent

    def save_manage():
        try:
            conn = get_connection()
            cur = conn.cursor()
            q = """
                INSERT INTO MANAGE (supervisor_id, train_number)
                VALUES (%s,%s)
            """
            cur.execute(q, (
                entries["Supervisor ID"].get(),
                entries["Train Number"].get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Supervisor assigned to train!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save_manage).grid(
        row=len(labels), column=0, columnspan=2, pady=10
    )

def view_manage_window():
    win = tk.Toplevel(root)
    win.title("Manage (Supervisor–Train)")
    win.geometry("900x400")

    cols = ("Supervisor", "Train No", "Train Name")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=150)

    try:
        conn = get_connection()
        cur = conn.cursor()
        q = """
            SELECT
                CONCAT(S.fname,' ',S.lname) AS supervisor_name,
                M.train_number,
                TD.train_name
            FROM MANAGE M
            JOIN TECHNICAL_SUPERVISOR S ON M.supervisor_id = S.supervisor_id
            JOIN TRAIN_DETAILS TD ON M.train_number = TD.train_number
        """
        cur.execute(q)
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================== MAIN WINDOW ==================
root = tk.Tk()
root.title("Railway Management System")
root.geometry("420x550")

title_lbl = tk.Label(root, text="Railway Management System", font=("Arial", 16, "bold"))
title_lbl.pack(pady=15)

btns = [
    ("Add Passenger", add_passenger_window),
    ("View Passengers", view_passengers_window),
    ("Add Train", add_train_window),
    ("View Trains", view_trains_window),
    ("Add Supervisor", add_supervisor_window),
    ("View Supervisors", view_supervisors_window),
    ("Issue Ticket", issue_ticket_window),
    ("View Tickets", view_tickets_window),
    ("Record Payment", record_payment_window),
    ("View Payments", view_payments_window),
    ("Record Check", record_check_window),
    ("View Checks", view_checks_window),
    ("Assign Supervisor to Train", assign_manage_window),
    ("View Manage (Supervisor–Train)", view_manage_window),
]

for text, cmd in btns:
    tk.Button(root, text=text, width=32, command=cmd).pack(pady=3)

root.mainloop()
