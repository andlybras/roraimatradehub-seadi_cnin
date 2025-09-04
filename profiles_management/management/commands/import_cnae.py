import csv
from django.core.management.base import BaseCommand
from profiles_management.models import CNAE

class Command(BaseCommand):
    help = 'Importa os códigos CNAE a partir de um arquivo CSV, lendo por posição da coluna.'

    def handle(self, *args, **kwargs):
        file_path = 'cnae_data.csv'
        
        CNAE.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Tabela de CNAEs limpa com sucesso.'))

        try:
            with open(file_path, 'r', encoding='latin-1') as csv_file:
                # Usando csv.reader para ler as linhas como listas, ignorando os cabeçalhos
                reader = csv.reader(csv_file, delimiter=';')
                
                # Pula a linha do cabeçalho
                next(reader, None)  
                
                cnaes_to_create = []
                for row in reader:
                    # Tenta ler os dados pela posição da coluna.
                    # row[4] é a 5ª coluna (código), row[5] é a 6ª coluna (descrição).
                    try:
                        codigo_cnae = row[4]
                        descricao_cnae = row[5]

                        if codigo_cnae and descricao_cnae:
                            cnaes_to_create.append(
                                CNAE(codigo=codigo_cnae.strip(), descricao=descricao_cnae.strip())
                            )
                    except IndexError:
                        # Ignora linhas que não tenham colunas suficientes (linhas em branco, etc.)
                        pass

                CNAE.objects.bulk_create(cnaes_to_create)
                
                if len(cnaes_to_create) > 0:
                    self.stdout.write(self.style.SUCCESS(f'{len(cnaes_to_create)} códigos CNAE importados com sucesso!'))
                else:
                    self.stdout.write(self.style.ERROR('Nenhum código CNAE foi importado. Verifique se o arquivo CSV não está vazio e se o delimitador é ponto e vírgula (;).'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado em: {file_path}.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro inesperado: {e}'))