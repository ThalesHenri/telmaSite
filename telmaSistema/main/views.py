from django.shortcuts import render,  HttpResponse, get_object_or_404, redirect
from .forms import ProdutoForm, ClienteForm, ComprasForm
from .models import Produto, Cliente, Compras
from django.contrib import messages


def home(response):
    return render(response,'index.html')


def cadastrarProdutos(response):
    form = ProdutoForm()
    context = {'form':form}
    return render(response,'cadastroProdutos.html', context)

 
def cadastrarClientes(response):
    form = ClienteForm()
    context = {'form': form}
    return render(response, 'cadastroCliente.html', context)


def cadastrarCompras(response):
    form = ComprasForm()
    context = {'form': form}
    return render(response, 'cadastroCompras.html', context)


def mostrarProdutos(response):
    produto = Produto.objects.all()
    context = {'mostrarProdutos': produto}
    return render(response, 'mostrarProdutos.html', context)


def mostrarClientes(response):
    cliente = Cliente.objects.all()
    context = {'mostrarClientes': cliente}
    return render(response, 'mostrarClientes.html', context)


def mostrarCompras(response):
    compras = Compras.objects.all()
    context = {'mostrarCompras': compras}
    return render(response, 'mostrarCompras.html', context)


def cadastrarProdutosEvent(response):
    if response.method == 'POST':
        form = ProdutoForm(response.POST, response.FILES)
        if form.is_valid():
            produto = form.save()
            return HttpResponse('Produto cadastrado com sucesso!<br><a href="/">Voltar</a>')
    return HttpResponse('failed<br><a href="/">Voltar</a>')


def cadastrarClientesEvent(response):
    if response.method == 'POST':
        form = ClienteForm(response.POST)
        if form.is_valid():
            cliente = form.save()
            return HttpResponse('Cliente cadastrado com sucesso!<br><a href="/">Voltar</a>')
    return HttpResponse('failed')


def cadastrarComprasEvent(response):
    if response.method == 'POST':
        form = ComprasForm(response.POST)
        if form.is_valid():
            compras = form.save()
            return HttpResponse('Compra cadastrada com sucesso!<br><a href="/">Voltar</a>')
    return HttpResponse('failed<br><a href="/">Voltar</a>')


def marcar_pagamento(response, id):
    compra = get_object_or_404(Compras, pk=id)
    compra.pagamento = True
    compra.save()
    return redirect('/mostrarCompras/')

def editarProduto(response, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if response.method == 'POST':
        form = ProdutoForm(response.POST, response.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(response, 'Produto atualizado com sucesso!')
            return redirect('mostrarProdutos')  # Redireciona para a lista de produtos ou para onde desejar
    else:
        form = ProdutoForm(instance=produto)

    return render(response, 'editarProduto.html', {'form': form, 'produto': produto})


def deletarProduto(response, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if response.method == 'POST':
        produto.delete()
        messages.success(response, 'Produto excluído com sucesso!')
        return redirect('mostrarProdutos')  # Redireciona para a lista de produtos ou para onde desejar

    return render(response, 'confirmarDelete.html', {'produto': produto})



def editarCliente(response, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if response.method == 'POST':
        form = ClienteForm(response.POST, response.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(response, 'Cliente atualizado com sucesso!')
            return redirect('mostrarClientes')  # Redireciona para a lista de produtos ou para onde desejar
    else:
        form = ClienteForm(instance=cliente)

    return render(response, 'editarCliente.html', {'form': form, 'cliente': cliente})


def deletarCliente(response, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if response.method == 'POST':
        cliente.delete()
        messages.success(response, 'Cliente excluído com sucesso!')
        return redirect('mostrarClientes')  

    return render(response, 'confirmarDelete.html', {'cliente': cliente})


def editarCompras(response, pk):
    compras = get_object_or_404(Compras, pk=pk)

    if response.method == 'POST':
        form = ComprasForm(response.POST, response.FILES, instance=compras)
        if form.is_valid():
            form.save()
            messages.success(response, 'Compras atualizado com sucesso!')
            return redirect('mostrarComprass')  
    else:
        form = ComprasForm(instance=compras)

    return render(response, 'editarCompras.html', {'form': form, 'compras': compras})


def deletarCompras(response, pk):
    compras = get_object_or_404(Compras, pk=pk)

    if response.method == 'POST':
        compras.delete()
        messages.success(response, 'Compras excluído com sucesso!')
        return redirect('mostrarCompras')  

    return render(response, 'confirmarDelete.html', {'compras': compras})


def ajuda(response):
    return render(response,'ajuda.html')