from django.shortcuts import render

from admin_panel.decorators import admin_required


@admin_required
def admin_dashboard(request):
    return render(
        request,
        template_name="dashboard.html",
    )


@admin_required
def admin_products(request):
    return render(
        request,
        template_name="products.html",
    )

