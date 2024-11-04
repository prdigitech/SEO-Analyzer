

# SEO Analyzer

A simple SEO analysis tool built with Python that audits key elements of a website's SEO, including Title Tags, Meta Descriptions, Header Tags, and Image Alt Tags. This project provides insights into SEO improvements.

## Features

- Analyze the **Title Tag** of a webpage
- Retrieve and display the **Meta Description**
- List all **Header Tags** (H1, H2, H3, etc.)
- Check for **Image Alt Tags** and report any missing ones

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup 4 library

## Installation

1. Clone the repository:
   
2. Create and activate a virtual environment:
   
3. Install the required dependencies:

## Usage

Run the SEO Analyzer by executing the following command:

When prompted, enter the URL of the website you want to analyze. The tool will display the results of the SEO audit.

## Example


Enter the URL of the website: https://example.com
Title Tag: Example Domain
Meta Description: This domain is for use in illustrative examples in documents.
H1: ['Example Domain']
H2: []
H3: []
Images missing Alt Tags: ['/images/logo.png']


## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Pratik Pawan Ramdasi** - [GitHub Profile](https://github.com/Pratik-Ramdasi)


```bash
git clone https://github.com/Pratik-Ramdasi/seo-analyzer.git
cd seo-analyzer
```
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install requests beautifulsoup4
```
```bash
python app.py
```
