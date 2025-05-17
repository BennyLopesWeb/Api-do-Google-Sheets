from pprint import pprint

def read_sheet(service, spreadsheet_id, range_name):
    """Lê dados da planilha."""
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name
        ).execute()
        values = result.get('values', [])
        if not values:
            print('⚠️ Nenhum dado encontrado.')
        else:
            print('📥 Dados encontrados:')
            pprint(values)
        return values
    except Exception as e:
        print(f'❌ Erro ao ler dados: {e}')


def write_to_sheet(service, spreadsheet_id, range_name, values):
    """Escreve dados na planilha."""
    try:
        body = {'values': values}
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
        print(f"✅ {result.get('updatedCells')} células atualizadas.")
    except Exception as e:
        print(f'❌ Erro ao escrever dados: {e}')
