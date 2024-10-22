
![Logo](tdc-summit-brasilia.png)


# Moment How To - Criando Servidor IA com FastAPI.

Libere o potencial de sua IA. Crie sua API de IA com FastAPI.

FastAPI é um framework web Python moderno, rápido e fácil de usar, perfeito para construir APIs para seus modelos. Vamos construir juntos uma API que expõe endpoints para sua aplicação.


## 🚀Marcelo Markus
Analista de Sistemas, apaixonado por tecnologia.    

Desenvolvedor na AltoQI - Solução Bim para Engenharia.

https://www.linkedin.com/in/marcelo-markus-27929374/


## Roadmap



## Instalação

Clone o repositório:

```bash
  git clone
```

Instalar UV - Project Manager (https://docs.astral.sh/uv/):

macOs/Linux
```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
```
Windows
```bash
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Criar ambiente virtual com UV:

```bash
  uv venv
```

Para sincronizar as dependências do projeto com venv, execute:

```bash
  uv sync
```

## API IA Reference

#### 1- Endpoint GET utilizando Openai (chat)

```http
  GET /ia/openai
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `question` | `string` | **Required**. Question |

#### 2- Endpoint GET utilizando Groq (chat)

```http
  GET /ia/groq
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `question` | `string` | **Required**. Question |

#### 3- Endpoint GET utilizando Groq (trascription audio)

```http
  GET /ia/groq/audio
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `audio` | `file` | **Required**. Audio wave |
| `question` | `string` | **Required**. Question |

