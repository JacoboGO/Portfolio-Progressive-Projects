import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

#Configuración de volumen de datos
num_orders = 250000 

#1. Generación de dimensión de productos (productos_dim.csv)
products_data = {
    'product_id': [f'P{str(i).zfill(3)}' for i in range(1, 11)],
    'product_name': ['Monitor 24', 'Silla Erg', 'Teclado Mec', 'Escritorio', 'Mause Gam', 'Laptop pro','Cable HDMI','Hub USB','Soporte Monitor','Lampara Led'],
    'category': ['ELECTRÓNICA', ' Muebles ', 'electronica', 'MUEBLES', 'electronica', 'ELECTRONICA','Accesorios',' accesorios ','Muebles','ELECTRONICA'],
    'unit_cost': [150.0, 80.0, 30.0, 120.0, 15.0, 800.0, 10.0, 20.0, 45.0, 25.0],
    'unit_price': [250.0, 180.0, 75.0, 300.0, 45.0, 1200.0, 25.0, 45.0, 85.0, 55.0],
    'lead_time_target': [5,10,5,10,5,7,3,3,7,5]
}
df_products = pd.DataFrame(products_data)
df_products.to_csv(r'C:\Users\JGO Gamer\Documents\Projects\Proyecto base\data\raw\products_dim.csv', index=False)

#2. Generación de hecho de ventas (orders_raw.csv)
order_ids = range(10001, 10001 + num_orders)
start_date = datetime(2026, 1, 1)

data_orders = []
for i in range(num_orders):
    order_date = start_date + timedelta(days=random.randint(0, 150))
    #Introducir inconcistencias en formatos de fecha (10% de los casos)
    if random.random() < 0.10:
        o_date_str = order_date.strftime('%d-%m-%Y')  # Formato inconsistente
    else:
        o_date_str = order_date.strftime('%Y-%m-%d')  # Formato consistente

    # Simular Lead Time (Tiempo de envío) con OUTLIERS
    lead_time = random.randint(1, 5)
    if random.random() < 0.03:  # 3% de los casos con lead time extremo (retrasos masivos)
        lead_time = random.randint(20, 45)

    ship_date = order_date + timedelta(days=lead_time)

    data_orders.append([
        order_ids[i],
        o_date_str,
        f'P{str(random.randint(1, 10)).zfill(3)}',
        random.randint(1, 15),
        f'C{random.randint(500, 2000)}',
        ship_date.strftime('%Y-%m-%d') if random.random() > 0.01 else '', #1% nulos
        random.choice(['Norte', 'Sur', 'Centro', 'Este', 'Oeste'])
    ])

df_orders = pd.DataFrame(data_orders, columns=['order_id', 'order_date', 'product_id', 'quantity', 'customer_id', 'ship_date', 'store_region'])
df_orders.to_csv(r'C:\Users\JGO Gamer\Documents\Projects\Proyecto base\data\raw\orders_raw.csv', index=False)

#3. Generación de Estatus de Inventario (inventory_status.csv)
inventory_data = {
    'product_id': [f'P{str(i).zfill(3)}' for i in range(1, 11)],
    'current_stock': [random.randint(0, 200) for _ in range(10)],
    'warehouse_location': [random.choice(['Bodega A', 'Bodega B', 'Bodega C']) for _ in range(10)],
    'min_stock_level': [random.randint(10, 30) for _ in range(10)],
}

df_inventory = pd.DataFrame(inventory_data)
df_inventory.to_csv(r'C:\Users\JGO Gamer\Documents\Projects\Proyecto base\data\raw\inventory_status.csv', index=False)

print(f"✅ éxito: Se han generado {num_orders} registros en data/raw/")



