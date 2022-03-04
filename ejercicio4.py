
persona = {
    "datospersonales": {
        "nombre": "Marlon",
        "apellido": "Alarcon",
        "edad": 22,
    },

    "salarial": {
        "salario": 2000000,
        "subtranporte": 50000,
        "subalimentacion": 60000
    }
}

print(persona["salarial"])
print (f"Nombre: {persona ['datospersonales']['nombre']})

if __name__ == "__main__":
    main()