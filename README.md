PY-SINAIS
=========

Este é um projeto da disciplina de Sinais e Sistemas Dinâmicos e foi pensado para aplicação de filtros de frequência em arquivos de audio.

O projeto é dividido em 3 scripsts em python 3:
- convert-wav.py
- low-pass.py
- main.py


---

Módulo convert-wav
------------------

É utilizado para converter arquivos _.mp3_ em _.wav_ para que possam ser analisados nos outros módulos.

Uso:

>$ python3 convert-wav.py audio_em_mp3


---

Módulo low-pass
---------------

Implementa um módulo de filtro passa-baixa, mas pode ser modificado para ser um passa-alta em parâmentros internos do código.

Plota o Espectrograma do sinal antes e depois da aplicação no filtro em arquivos _.png_.

Uso:

>$ python3 low-pass.py audio_em_wav


---

Módulo principal (main)
-----------------------

Implementa as principais funcionalidades do módulo.

Ao ser chamado, plota gráficos do sinal no domínio do tempo, da frequência e espetrogramas dos canais. Ainda aplica uma filtragem de largura de banda salvando arquivos de audio com frequêcias delimitadas em 200 Hz (parâmetro ajustável no código).

Uso:

>$ python3 main.py audio_em_wav


---

Requisitos
----------

- Python 3
- Módulo numpy
- Módulo scipy
- Módulo pydub
- Módulo matplotlib

