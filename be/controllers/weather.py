"""Controller for weather_data endpoint of fake wiga."""
import pandas as pd

from ..api.api_schemas import WeatherInSchema


def read_weather_file(filters: WeatherInSchema) -> list[dict]:
    """Read and format weather data according to filters."""
    df = pd.read_excel("be/controllers/stored_data/weather_update_test.xlsx")
    df["space"] = " "
    df["time"] = df["Fecha"] + df["space"] + df["Hora"]
    df["time"] = pd.to_datetime(df["time"])

    sensor_ids = {
        330: "Humedad Relativa EST Caribe - Antioquia %",
        331: "Radiación Par EST Caribe - Antioquia µmol m-2 s-1",
        332: "Temperatura EST Caribe - Antioquia °C",
    }
    try:
        columns = [sensor_ids[wanted_id] for wanted_id in filters.ids_sensores] + ["time"]
        df = df[columns]
    except KeyError as e:
        return [{"message": f"Invalid sensor ID {e}"}]

    initial_date = filters.fecha_inicio
    final_date = filters.fecha_fin
    try:
        df = df[(initial_date <= df["time"]) & (df["time"] <= final_date)]
    except TypeError as e:
        return [{"message": f"Invalid date format {e}"}]

    df["time"] = df["time"].astype(str)
    weather_data = []
    for sensor_id in filters.ids_sensores:
        sensor_dict = {}
        sensor_dict["id_sensor"] = sensor_id
        sensor_dict["nombre"] = sensor_ids[sensor_id]
        subdf = df[["time", sensor_dict["nombre"]]].copy()
        subdf.columns = ["fecha", "valor"]
        subdf["id_wiga_dato"] = subdf.index
        datos = subdf.to_dict(orient="records")
        sensor_dict["datos"] = datos
        weather_data.append(sensor_dict)
    return weather_data
