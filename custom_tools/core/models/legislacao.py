from pydantic import BaseModel, Field

class Legislacao(BaseModel):
    identificador: str = Field(..., description="Identificador da legislação na origem")
    origem: str = Field(..., description="Identificador da origem")
    palavras_chaves:str =  Field(..., description="palalavras chaves")
    urn: str = Field(..., description="urn na API do Senado Federal")
    nome_alternativo: str = Field(..., description="Nome alternativo")
    data_publicacao: str = Field(..., description="Data de Publicação")
    tipo_legislacao: str = Field(..., description="Tipo de Legislacao")
    titulo: str = Field(..., description="Título da legislacao")
    ementa: str = Field(..., description="Ementa do documento")
    conteudo: str = Field(..., description="Conteúdo do documento")
