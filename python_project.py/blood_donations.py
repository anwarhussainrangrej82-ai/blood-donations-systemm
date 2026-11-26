import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class BloodDonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🩸 Blood Donation Management System")
        self.root.geometry("950x620")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(False, False)

        # ========== PRE-LOADED DATA (Jodhpur + Udaipur) ==========
        self.donors = [
            {
                "name": "Rahul Sharma",
                "contact": "9876543210",
                "age": "28",
                "address": "Sardarpura, Jodhpur",
                "blood_group": "B+"
            },
            {
                "name": "Priya Meena",
                "contact": "9123456789",
                "age": "24",
                "address": "Ratanada, Jodhpur",
                "blood_group": "O+"
            },
            {
                "name": "Amit Singh",
                "contact": "9988776655",
                "age": "32",
                "address": "Shastri Circle, Udaipur",
                "blood_group": "A+"
            },
            {
                "name": "Neha Joshi",
                "contact": "9765432109",
                "age": "26",
                "address": "Hiran Magri, Udaipur",
                "blood_group": "AB+"
            },
            {
                "name": "Vikram Rathore",
                "contact": "9898989898",
                "age": "35",
                "address": "Chopasni Housing Board, Jodhpur",
                "blood_group": "O-"
            }
        ]

        # Inventory automatically set according to pre-loaded donors
        self.inventory = {
            "A+": 0, "A-": 0, "B+": 0, "B-": 0,
            "AB+": 0, "AB-": 0, "O+": 0, "O-": 0
        }
        for donor in self.donors:
            self.inventory[donor["blood_group"]] += 1

        self.create_widgets()

    def create_widgets(self):
        # ===== Header =====
        header = tk.Frame(self.root, bg="#e94560", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header, 
            text="🩸 BLOOD DONATION MANAGEMENT SYSTEM",
            font=("Segoe UI", 22, "bold"),
            bg="#e94560",
            fg="white"
        )
        title.pack(pady=20)

        # ===== Main Content =====
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left Side - Buttons
        left_frame = tk.Frame(main_frame, bg="#16213e", width=280)
        left_frame.pack(side="left", fill="y", padx=(0, 15))
        left_frame.pack_propagate(False)

        tk.Label(
            left_frame, 
            text="OPTIONS", 
            font=("Segoe UI", 14, "bold"),
            bg="#16213e", 
            fg="#e94560"
        ).pack(pady=(25, 15))

        buttons = [
            ("➕  Add New Donor", self.add_donor, "#0f3460"),
            ("🗑️  Remove Donor", self.remove_donor, "#0f3460"),
            ("📦  View Inventory", self.view_inventory, "#0f3460"),
            ("👥  View All Donors", self.view_donors, "#0f3460"),
            ("🔍  Search by Blood Group", self.search_blood, "#0f3460"),
            ("❌  Exit", self.exit_app, "#e94560"),
        ]

        for text, command, color in buttons:
            btn = tk.Button(
                left_frame,
                text=text,
                font=("Segoe UI", 12, "bold"),
                bg=color,
                fg="white",
                activebackground="#e94560",
                activeforeground="white",
                relief="flat",
                cursor="hand2",
                command=command,
                height=2
            )
            btn.pack(fill="x", padx=20, pady=8)

            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#e94560"))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))

        # Right Side - Display Area
        right_frame = tk.Frame(main_frame, bg="#16213e")
        right_frame.pack(side="right", fill="both", expand=True)

        tk.Label(
            right_frame,
            text="DISPLAY PANEL",
            font=("Segoe UI", 14, "bold"),
            bg="#16213e",
            fg="#e94560"
        ).pack(pady=(20, 10))

        self.display = tk.Text(
            right_frame,
            font=("Consolas", 11),
            bg="#0f3460",
            fg="#eaeaea",
            relief="flat",
            padx=15,
            pady=15,
            wrap="word"
        )
        self.display.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.show_welcome()

    def clear_display(self):
        self.display.delete("1.0", tk.END)

    def show_welcome(self):
        self.clear_display()
        self.display.insert(tk.END, "Welcome to Blood Donation Management System!\n\n")
        self.display.insert(tk.END, "➤ 5 Sample Donors pehle se loaded hain (Jodhpur + Udaipur)\n")
        self.display.insert(tk.END, "➤ Add New Donor → Extra donors add kar sakte ho\n")
        self.display.insert(tk.END, "➤ Remove Donor → Donor delete + inventory se unit kam\n")
        self.display.insert(tk.END, "➤ View Inventory / View All Donors se check karo\n\n")
        self.display.insert(tk.END, "System ready hai... 🩸")

    # ==================== ADD DONOR ====================
    def add_donor(self):
        add_win = tk.Toplevel(self.root)
        add_win.title("Add New Donor")
        add_win.geometry("420x520")
        add_win.configure(bg="#1a1a2e")
        add_win.resizable(False, False)
        add_win.grab_set()

        tk.Label(
            add_win, 
            text="➕ Add New Donor", 
            font=("Segoe UI", 16, "bold"),
            bg="#1a1a2e", 
            fg="#e94560"
        ).pack(pady=15)

        fields = {}

        def create_field(label_text):
            tk.Label(add_win, text=label_text, font=("Segoe UI", 11), 
                     bg="#1a1a2e", fg="white").pack(pady=(8, 2))
            entry = tk.Entry(add_win, font=("Segoe UI", 12), width=32, justify="center")
            entry.pack(pady=2)
            return entry

        fields["name"] = create_field("Donor Name:")
        fields["name"].focus()
        fields["contact"] = create_field("Contact Number:")
        fields["age"] = create_field("Age:")
        fields["address"] = create_field("Address:")

        tk.Label(add_win, text="Blood Group:", font=("Segoe UI", 11), 
                 bg="#1a1a2e", fg="white").pack(pady=(10, 2))
        
        blood_var = tk.StringVar(value="A+")
        blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        
        blood_menu = ttk.Combobox(
            add_win, 
            textvariable=blood_var, 
            values=blood_groups, 
            state="readonly",
            font=("Segoe UI", 12),
            width=30
        )
        blood_menu.pack(pady=2)

        def save_donor():
            name = fields["name"].get().strip()
            contact = fields["contact"].get().strip()
            age = fields["age"].get().strip()
            address = fields["address"].get().strip()
            blood = blood_var.get()

            if not name:
                messagebox.showwarning("Error", "Name cannot be empty!", parent=add_win)
                return
            if not contact:
                messagebox.showwarning("Error", "Contact Number is required!", parent=add_win)
                return
            if not age.isdigit() or int(age) < 18 or int(age) > 65:
                messagebox.showwarning("Error", "Age must be between 18 to 65!", parent=add_win)
                return
            if not address:
                messagebox.showwarning("Error", "Address is required!", parent=add_win)
                return

            donor = {
                "name": name,
                "contact": contact,
                "age": age,
                "address": address,
                "blood_group": blood
            }
            self.donors.append(donor)
            self.inventory[blood] += 1

            messagebox.showinfo("Success", 
                f"Donor '{name}' ({blood}) successfully added!\nInventory updated.", 
                parent=add_win)
            add_win.destroy()
            self.view_inventory()

        save_btn = tk.Button(
            add_win,
            text="✅ Save Donor",
            font=("Segoe UI", 12, "bold"),
            bg="#e94560",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=save_donor,
            width=20,
            height=2
        )
        save_btn.pack(pady=25)

    # ==================== REMOVE DONOR ====================
    def remove_donor(self):
        if not self.donors:
            messagebox.showinfo("Info", "No donors available to remove!")
            return

        self.view_donors()

        index = simpledialog.askinteger(
            "Remove Donor",
            "Enter Donor Number (No.) to remove:",
            parent=self.root,
            minvalue=1,
            maxvalue=len(self.donors)
        )

        if index is None:
            return

        donor = self.donors[index - 1]
        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Kya aap is donor ko delete karna chahte ho?\n\n"
            f"Name      : {donor['name']}\n"
            f"Blood     : {donor['blood_group']}\n"
            f"Contact   : {donor['contact']}"
        )

        if confirm:
            blood = donor["blood_group"]
            if self.inventory[blood] > 0:
                self.inventory[blood] -= 1

            del self.donors[index - 1]

            messagebox.showinfo("Deleted", 
                f"Donor '{donor['name']}' successfully removed!\n"
                f"{blood} unit inventory se kam ho gayi.")
            self.view_inventory()

    # ==================== VIEW INVENTORY ====================
    def view_inventory(self):
        self.clear_display()
        self.display.insert(tk.END, "📦 CURRENT BLOOD INVENTORY\n")
        self.display.insert(tk.END, "=" * 45 + "\n\n")

        total = 0
        for group, units in self.inventory.items():
            status = "🟢" if units > 0 else "🔴"
            self.display.insert(tk.END, f"  {status}  {group:<6}  →  {units} unit(s)\n")
            total += units

        self.display.insert(tk.END, "\n" + "=" * 45 + "\n")
        self.display.insert(tk.END, f"  Total Units Available : {total}\n")
        self.display.insert(tk.END, "=" * 45)

    # ==================== VIEW ALL DONORS ====================
    def view_donors(self):
        self.clear_display()
        self.display.insert(tk.END, "👥 REGISTERED DONORS (Full Details)\n")
        self.display.insert(tk.END, "=" * 70 + "\n\n")

        if not self.donors:
            self.display.insert(tk.END, "  No donors registered yet.\n")
            return

        for i, donor in enumerate(self.donors, 1):
            self.display.insert(tk.END, f"  [{i}]  {donor['name']}\n")
            self.display.insert(tk.END, f"       Blood Group : {donor['blood_group']}\n")
            self.display.insert(tk.END, f"       Contact     : {donor['contact']}\n")
            self.display.insert(tk.END, f"       Age         : {donor['age']}\n")
            self.display.insert(tk.END, f"       Address     : {donor['address']}\n")
            self.display.insert(tk.END, "-" * 55 + "\n")

        self.display.insert(tk.END, f"\n  Total Donors : {len(self.donors)}")

    # ==================== SEARCH ====================
    def search_blood(self):
        blood = simpledialog.askstring(
            "Search", 
            "Enter Blood Group (A+, A-, B+, B-, AB+, AB-, O+, O-):",
            parent=self.root
        )

        if not blood:
            return

        blood = blood.strip().upper()

        if blood not in self.inventory:
            messagebox.showerror("Error", "Invalid Blood Group!")
            return

        found = [d for d in self.donors if d["blood_group"] == blood]

        self.clear_display()
        self.display.insert(tk.END, f"🔍 DONORS WITH BLOOD GROUP : {blood}\n")
        self.display.insert(tk.END, "=" * 55 + "\n\n")

        if not found:
            self.display.insert(tk.END, f"  No donors found with blood group {blood}\n")
        else:
            for donor in found:
                self.display.insert(tk.END, f"  • {donor['name']}\n")
                self.display.insert(tk.END, f"    Contact : {donor['contact']}\n")
                self.display.insert(tk.END, f"    Address : {donor['address']}\n")
                self.display.insert(tk.END, f"    Age     : {donor['age']}\n\n")
            self.display.insert(tk.END, f"  Total Found : {len(found)}")

    def exit_app(self):
        if messagebox.askyesno("Exit", "Kya aap system band karna chahte hain?"):
            self.root.destroy()


# ===== Run the App =====
if __name__ == "__main__":
    root = tk.Tk()
    app = BloodDonationApp(root)
    root.mainloop()