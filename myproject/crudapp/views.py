from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Item

# List items
def index(request):
    items = Item.objects.all()
    return render(request, 'crudapp/index.html', {'items': items})

# Add a new item
def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        country = request.POST.get('country')  # Get the selected country from the dropdown
        Item.objects.create(name=name, description=description, country=country)
        return redirect('index')
    countries = ["United States", "Canada", "United Kingdom", "Australia", "India"]  # List of countries
    return render(request, 'crudapp/add_item.html', {'countries': countries})

# Edit an item
def edit_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.country = request.POST.get('country')  # Update the selected country
        item.save()
        return redirect('index')
    countries = ["United States", "Canada", "United Kingdom", "Australia", "India"]
    return render(request, 'crudapp/edit_item.html', {'item': item, 'countries': countries})

# Delete an item
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('index')

# Generate a PDF with the items
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="items.pdf"'
    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Add content to the PDF
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "Items List")
    pdf.setFont("Helvetica", 12)

    items = Item.objects.all()
    y = height - 100
    for item in items:
        pdf.drawString(50, y, f"Name: {item.name}")
        pdf.drawString(50, y - 20, f"Description: {item.description}")
        pdf.drawString(50, y - 40, f"Country: {item.country}")
        y -= 80
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = height - 50

    pdf.save()
    return response
