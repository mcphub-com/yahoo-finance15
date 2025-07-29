import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/sparior/api/yahoo-finance15'

mcp = FastMCP('yahoo-finance15')

@mcp.tool()
def market_tickers(type: Annotated[str, Field(description='Enter one of the following assetClass: STOCKS or ETF or MUTUALFUNDS. Example: STOCKS')],
                   page: Annotated[Union[int, float, None], Field(description='Enter a page number. Default: 1')] = None) -> dict: 
    '''Get ticker symbols for stocks traded in the U.S exchange'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v2/markets/tickers'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_search(search: Annotated[str, Field(description='')]) -> dict: 
    '''Get tickers for any stock company, ETF, mutual fund, crypto and more'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/search'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_quotes(ticker: Annotated[str, Field(description='Enter a ticker (one only)')],
                  type: Annotated[str, Field(description='Enter one of the following assetClass: STOCKS or ETF or MUTUALFUNDS . Example: STOCKS')]) -> dict: 
    '''Real-time Quote data for stocks, ETFs, mutual funds, etc...'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/quote'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_history(symbol: Annotated[str, Field(description='A single symbol')],
                  interval: Annotated[str, Field(description='Allows one of following : 5m|15m|30m|1h|1d|1wk|1mo|3mo')],
                  diffandsplits: Annotated[Union[str, None], Field(description='Allows one of following : true|false')] = None) -> dict: 
    '''Historic data for stocks, ETFs, mutual funds, etc...'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'interval': interval,
        'diffandsplits': diffandsplits,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_screener(list: Annotated[str, Field(description="Select one of these options: trending Trending tickers in today's market undervalued_growth_stocks Stocks with earnings growth growth_technology_stocks Technology stocks with revenue day_gainers Stocks with the highest gains day_losers Stocks with the highest losses most_actives Stocks by intraday trade volume. undervalued_large_caps Undervalued large cap stocks aggressive_small_caps Small-cap stocks with earnings growth. small_cap_gainers Small caps with a 1 day price change of 5.0%")]) -> dict: 
    '''Get a collection of stocks, ETFs, and mutual funds based on selected criteria.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/screener'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list': list,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_modules(ticker: Annotated[str, Field(description='')],
                  module: Annotated[str, Field(description='Acceptable values: (one per request) profile income-statement balance-sheet cashflow-statement statistics calendar-events sec-filings recommendation-trend upgrade-downgrade-history institution-ownership fund-ownership major-directHolders major-holders-breakdown insider-transactions insider-holders net-share-purchase-activity earnings industry-trend index-trend sector-trend')]) -> dict: 
    '''Get combine stock data such as profile, financial data, statistics, balance sheet, sec-filing, quote, earnings, trends and more!'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
        'module': module,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_insider_trades() -> dict: 
    '''Latest insider trading activities from CEO, Directors, Chief Executive Officer, 10% Owner, etc...'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/insider-trades'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_news(tickers: Annotated[Union[str, None], Field(description='A stock symbol')] = None,
                type: Annotated[Union[str, None], Field(description='Enter one of the following types: ALL or VIDEO or PRESS_RELEASE')] = None) -> dict: 
    '''Get market news and press releases for a given company.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v2/markets/news'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tickers': tickers,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_profile(ticker: Annotated[str, Field(description='Provide the company ticker')]) -> dict: 
    '''Get stock profile information such as company name, descriptions, website, etc...'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_statistics(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock key statistics data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_financial_data(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock financial data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_sec_filings(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock SEC filings.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_earnings(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get earnings information for a particular stock'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_calendar_events(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock calendar events.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_insider_holders(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock insider holders' information.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_balance_sheet(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock balance sheet data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_institution_ownership(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock institution ownership.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_insider_transactions(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock insider transactions history.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_index_trend(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get index trend earnings history information for a particular stock'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_income_statement(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock income statement data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_cashflow_statement(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock cash flow statements.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_recommendation_trend(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock recommendations and trends.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_net_share_purchase_activity(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get net share purchase activity information for a particular stock'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stock_upgrade_downgrade_history(ticker: Annotated[str, Field(description='')]) -> dict: 
    '''Get stock upgrade and downgrade history.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_earnings(ticker: Annotated[Union[str, None], Field(description='Provide the company ticker')] = None,
                      date: Annotated[Union[str, datetime, None], Field(description='Enter a calendar date, for example: 2023-11-30')] = None) -> dict: 
    '''Get past, present, and upcoming company earnings data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/calendar/earnings'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_dividends(ticker: Annotated[Union[str, None], Field(description='Provide the company ticker')] = None,
                       date: Annotated[Union[str, datetime, None], Field(description='Enter a calendar date, for example: 2023-11-30')] = None) -> dict: 
    '''Get past, present, and upcoming company dividend data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/calendar/dividends'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ticker': ticker,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_economic_events(date: Annotated[Union[str, datetime, None], Field(description='Enter a calendar date, for example: 2023-11-30')] = None) -> dict: 
    '''Get global economic events data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/calendar/economic_events'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_public_offerings(date: Annotated[Union[str, None], Field(description='Enter a calendar date, for example: 2023-11 (YYYY-MM)')] = None) -> dict: 
    '''Get the past, current and upcoming secondary public offerings (SPO) data.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/calendar/public_offerings'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_ipo(date: Annotated[Union[str, None], Field(description='Enter a calendar date, for example: 2023-11 (YYYY-MM)')] = None) -> dict: 
    '''Get the latest and upcoming IPO data. These companies are going public.'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/calendar/ipo'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar_stock_splits(date: Annotated[Union[str, None], Field(description='Enter a calendar date, for example: 2025-05-12 (YYYY-MM-DD)')] = None,
                          page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get the past, current, and upcoming stock splits'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/calendar/stock-splits'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def indicators_sma(symbol: Annotated[str, Field(description='A single symbol')],
                   interval: Annotated[str, Field(description='Select from : 5m|15m|30m|1h|1d|1wk|1mo|3mo')],
                   series_type: Annotated[str, Field(description='Select from : open | close | high | low')],
                   time_period: Annotated[str, Field(description='Number of data points used to calculate each moving average value. Positive integers are accepted.')],
                   limit: Annotated[Union[str, None], Field(description='Limit the number of results returned, default is 50')] = None) -> dict: 
    '''This technical indicator returns the simple moving average (SMA).'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/indicators/sma'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'interval': interval,
        'series_type': series_type,
        'time_period': time_period,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def indicators_rsi(symbol: Annotated[str, Field(description='A single symbol')],
                   interval: Annotated[str, Field(description='Select from : 5m|15m|30m|1h|1d|1wk|1mo|3mo')],
                   series_type: Annotated[str, Field(description='Select from : open | close | high | low')],
                   time_period: Annotated[str, Field(description='Number of data points used to calculate each moving average value. Positive integers are accepted.')],
                   limit: Annotated[Union[str, None], Field(description='Limit the number of results returned, default is 50')] = None) -> dict: 
    '''This technical indicator returns the relative strength index (RSI)'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/indicators/rsi'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'interval': interval,
        'series_type': series_type,
        'time_period': time_period,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def indicators_macd(symbol: Annotated[str, Field(description='A single symbol')],
                    interval: Annotated[str, Field(description='Select from : 5m|15m|30m|1h|1d|1wk|1mo|3mo')],
                    series_type: Annotated[str, Field(description='Select from : open | close | high | low')],
                    fast_period: Annotated[Union[str, None], Field(description='Enter the fast period. Positive integers are accepted. Default: 12')] = None,
                    slow_period: Annotated[Union[str, None], Field(description='Enter the slow period. Positive integers are accepted. Default: 26')] = None,
                    signal_period: Annotated[Union[str, None], Field(description='Enter the signal period. Positive integers are accepted. Default: 9')] = None,
                    limit: Annotated[Union[str, None], Field(description='Limit the number of results returned, default is 50')] = None) -> dict: 
    '''This technical indicator returns the moving average convergence/divergence (MACD)'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/indicators/macd'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'interval': interval,
        'series_type': series_type,
        'fast_period': fast_period,
        'slow_period': slow_period,
        'signal_period': signal_period,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def indicators_adx(symbol: Annotated[str, Field(description='A single symbol')],
                   interval: Annotated[str, Field(description='Select from : 5m|15m|30m|1h|1d|1wk|1mo|3mo')],
                   series_type: Annotated[str, Field(description='Select from : open | close | high | low')],
                   time_period: Annotated[str, Field(description='Number of data points used to calculate each moving average value. Positive integers are accepted.')],
                   limit: Annotated[Union[str, None], Field(description='Limit the number of results returned, default is 50')] = None) -> dict: 
    '''This technical indicator returns the average directional movement index (ADX).'''
    url = 'https://yahoo-finance15.p.rapidapi.com/api/v1/markets/indicators/adx'
    headers = {'x-rapidapi-host': 'yahoo-finance15.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'interval': interval,
        'series_type': series_type,
        'time_period': time_period,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
