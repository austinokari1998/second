import sys
class employee:
    pay_rise_percent=1.20
    def __init__(self, name,code , pay, email):
        self.name=name
        self.code=code
        self.pay=pay
        self.email=email
        
    def properinto(self):
        return '{} CODE: {} '.format(self.name, self.code)
    def payrise(self):
        self.pay=int(self.pay*pay_rise_percent)
        
class developer(employee):
    pay_rise_percent=1.50
    def __init__(self, name, code, pay, email, prog_lang):
        super(). __init__(name, code,pay, email)
        self.prog_lang=prog_lang
    @classmethod
    def easy_intro(cls, developer_str):
        name, code, pay, email, prog_lang=developer_str.split(',')
        return cls(name, code, pay, email, prog_lang)
    def __add__(self, other):
            return self.pay+other.pay
        
class manager(employee):
        def __init__(self, name, code, pay, email, employees=None):
            super(). __init__(name, code, pay, email)
            if employees is None:
                employees=[]
            else:
                self.employees=employees
        def add_emp(self, new_emp):
            if new_emp not in self.employees:
                self.employees.append(new_emp)
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)
                
        def no_of_emp(self):
            for emp in self.employees:
                print("------>" ,emp.properinto())
        @classmethod
        def easy_intro(cls, manager_str):
            name, code, pay, email,employees=manager_str.split(',')
            return cls(name, code, pay, email,employees)
        
            
ariri_str='ariri,11145,20000,ariri@gmail,python'
okari_str='okari,11163,200000,oakri@gmai.cp,python'
rorat_str='rorat,11144,1221121,qjkwhevd@gmail,python'
ariri=developer.easy_intro(ariri_str)
rorat=developer.easy_intro(rorat_str)
okari=developer.easy_intro(okari_str)
manager_1='thiago,6667,30000,thiago@gmail.com,[okari]'
thiago=manager.easy_intro(manager_1)
thiago.add_emp(rorat)
print(ariri+rorat)
