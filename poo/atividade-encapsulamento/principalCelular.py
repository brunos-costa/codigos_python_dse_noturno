from celular import Celular

meuCelular = Celular(12345678, 30)

meuCelular.exibirDados()
meuCelular.plano = "pós-pago"
meuCelular.fazerChamada(27)
meuCelular.exibirDados()

meuCelular.plano = "pré-pago"
meuCelular.recarregar(20)
meuCelular.fazerChamada(32)
meuCelular.exibirDados()