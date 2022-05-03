from dynaconf import Dynaconf
import os


settings = Dynaconf(
    envvar_prefix="BEERLOG",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)
