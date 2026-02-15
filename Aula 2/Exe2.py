premio_total = 780000.00

primeiro_ganhador = premio_total * 0.46
segundo_ganhador = premio_total * 0.32
terceiro_ganhador = premio_total - (primeiro_ganhador + segundo_ganhador)

print(f"Primeiro colocado: R$ {primeiro_ganhador:,.2f}")
print(f"Segundo colocado: R$ {segundo_ganhador:,.2f}")
print(f"Terceiro colocado: R$ {terceiro_ganhador:,.2f}")