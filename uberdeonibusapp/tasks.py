import asyncio
from datetime import datetime, timedelta
from .models import Poltrona

async def reservar_poltrona_assincrona(poltrona_id):
    # Lógica de reserva de poltrona
    poltrona = Poltrona.objects.get(pk=poltrona_id)

    if not poltrona.ocupada:
        # Reserva a poltrona
        poltrona.ocupada = True
        poltrona.save()

        print(f'Poltrona {poltrona.numero} reservada em {datetime.now()}')

        # Aguarda 5 minutos antes de liberar a poltrona
        await asyncio.sleep(300)

        # Libera a poltrona após o tempo especificado
        poltrona.ocupada = False
        poltrona.save()

        print(f'Poltrona {poltrona.numero} liberada em {datetime.now()}')
    else:
        print(f'Poltrona {poltrona.numero} já está ocupada')