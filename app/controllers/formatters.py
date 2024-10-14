def process_response(response):
    results = response.get("results", [])
    processed_results = []

    for result in results:
        columns = result.get("columns", [])
        rows = result.get("rows", [])
        
        for row in rows:
            entry = {columns[i]: row[i] for i in range(len(columns))}
            processed_results.append(entry)
    
    return processed_results