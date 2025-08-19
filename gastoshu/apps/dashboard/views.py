from django.shortcuts import render
from django.db.models import Sum
from apps.gastos.models import Gasto
from apps.ingresos.models import Ingresos


def inicio(request):
    total_gastos = Gasto.objects.aggregate(total=Sum("monto"))["total"] or 0
    total_ingresos = Ingresos.objects.aggregate(total=Sum("monto"))["total"] or 0
    balance = total_ingresos - total_gastos

    gastos = Gasto.objects.order_by("-fecha")[:5]
    ingresos = Ingresos.objects.order_by("-fecha")[:5]

    categorias = (
        Gasto.objects.values("categoria")
        .annotate(total=Sum("monto"))
        .order_by("-total")
    )
    total_gastos_categoria = sum(cat["total"] for cat in categorias)
    for cat in categorias:
        cat["porcentaje"] = (
            round((cat["total"] / total_gastos_categoria) * 100, 2)
            if total_gastos_categoria > 0
            else 0
        )

    context = {
        "total_gastos": total_gastos,
        "total_ingresos": total_ingresos,
        "balance": balance,
        "gastos": gastos,
        "ingresos": ingresos,
        "categorias": categorias,
    }
    return render(request, "index.html", context)
