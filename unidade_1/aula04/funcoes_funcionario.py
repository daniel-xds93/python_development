def desconto_inss(sal_bruto):
    return sal_bruto * 0.11

def desconto_va(sal_bruto):
    return sal_bruto * 0.05

def desconto_vt(sal_bruto):
    return sal_bruto * 0.06

def desconto_creche(sal_bruto):
    return sal_bruto * 0.15

def total_descontos(inss, va, vt, auxilio):
    return inss + va + vt + auxilio

def salario_liquido(sal_bruto, inss, va, vt, auxilio):
    return sal_bruto - total_descontos(inss, va, vt, auxilio)

