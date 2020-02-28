# Oil High Frequency Fundamentals

Pull high frequency (weekly) data for Oil Products.
Currently focused on Stocks


### Requirements

EIA data is pulled using the EIA API (for speed purposes)

An API key is needed to access the EIA's data, you can get one [here](https://www.eia.gov/opendata/register.php). eiapy needs this key to be manually set in the operating system environmental variables.
 
Set the key as an environment variable as follows;
```bash
export EIA_KEY=type_your_api_key_here
```

Remainder of the datasets are from Eikon and hence a terminal subscription is required

Follow instructions [here](https://developers.refinitiv.com/eikon-apis/eikon-data-apis/quick-start) to generate app key. 


Set the key as an environment variable as follows;
```bash
export EIKON_KEY=type_your_api_key_here
```
