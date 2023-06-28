import cx_Freeze
executables = [
    cx_Freeze.Executable(script="Main.py", icon="space.jpg")
]
cx_Freeze.setup(
    name = "Space Marker",
    options = {
        "build_exe":{
            "packages": ["pygame"],
            "include_files": [
                "fundo1.jpg",
                "space.png",
                "historico.txt",
                "Trilha.mp3"
            ]
        }
    } , executables = executables
)
# python geraSetup.py build
# python geraSetup.py bdist_msi