try:
    from pyscript import document
except ImportError:
    from js import document


non_metals = {
    "Hydrogen": ("H", 1, "1.008"),
    "Helium": ("He", 2, "4.0026"),
    "Carbon": ("C", 6, "12.011"),
    "Nitrogen": ("N", 7, "14.007"),
    "Oxygen": ("O", 8, "15.999"),
    "Fluorine": ("F", 9, "18.998"),
    "Neon": ("Ne", 10, "20.180"),
    "Phosphorus": ("P", 15, "30.974"),
    "Sulfur": ("S", 16, "32.06"),
    "Chlorine": ("Cl", 17, "35.45"),
    "Argon": ("Ar", 18, "39.948"),
    "Selenium": ("Se", 34, "78.971"),
    "Bromine": ("Br", 35, "79.904"),
    "Krypton": ("Kr", 36, "83.798"),
    "Iodine": ("I", 53, "126.90"),
    "Xenon": ("Xe", 54, "131.29"),
    "Radon": ("Rn", 86, "[222]"),
}


def find_element(event=None):
    result = document.getElementById("result")
    result.innerHTML = ""

    element1 = document.getElementById("element").value.strip().title()

    symbol, atomic_number, atomic_mass = non_metals.get(
        element1,
        ("Not found", "—", "—")
    )

    if element1 not in non_metals:
        result.innerHTML = f"<b>Element</b> {element1 or '—'}<br><b>Status</b> Element not found"
        return

    result.innerHTML = f"""
        <b>Symbol</b> {symbol}<br>
        <b>Element</b> {element1}<br>
        <b>Atomic Number</b> {atomic_number}<br>
        <b>Atomic Mass</b> {atomic_mass}
    """

