import argparse
from googleapiclient.discovery import build
from auth import get_credentials
from sheet_service import read_sheet, write_to_sheet
from utils import SPREADSHEET_ID, DEFAULT_RANGE, SAMPLE_DATA

def main():
    parser = argparse.ArgumentParser(description="Interage com a API do Google Sheets")
    parser.add_argument('--mode', choices=['read', 'write'], required=True, help='Modo de operação: read ou write')
    parser.add_argument('--range', default=DEFAULT_RANGE, help='Intervalo da planilha (ex: Página1!A1:D10)')
    args = parser.parse_args()

    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)

    if args.mode == 'read':
        read_sheet(service, SPREADSHEET_ID, args.range)
    elif args.mode == 'write':
        write_to_sheet(service, SPREADSHEET_ID, args.range, SAMPLE_DATA)

if __name__ == '__main__':
    main()
