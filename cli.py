import argparse
from pubmed_fetcher.core import fetch_pubmed_data

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma affiliations.")
    parser.add_argument("query", type=str, help="Query to search PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    data = fetch_pubmed_data(args.query)
    print(data)  # Placeholder for now