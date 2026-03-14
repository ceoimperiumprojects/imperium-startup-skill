# MCP Server Builder Guide

## What is MCP?
Model Context Protocol — a standard for connecting AI assistants to external tools, data sources, and services.

## MCP Server Structure

### Tool Definition
```json
{
  "name": "search_customers",
  "description": "Search for customers by name, email, or company. Returns matching customer records with contact info and recent activity.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term (name, email, or company name)"
      },
      "limit": {
        "type": "number",
        "description": "Maximum results to return (default: 10)",
        "default": 10
      }
    },
    "required": ["query"]
  }
}
```

## Tool Design Principles

### 1. Single Responsibility
Each tool does ONE thing well.
- Good: `search_customers`, `create_customer`, `update_customer`
- Bad: `manage_customers` (too broad)

### 2. Clear Descriptions
The description is how Claude decides which tool to use. Be specific:
- Good: "Search for customers by name, email, or company name"
- Bad: "Customer search"

### 3. Structured Input/Output
- Use JSON Schema for inputs
- Return structured JSON, not prose
- Include all relevant data in response
- Handle errors with clear error messages

### 4. Meaningful Defaults
- Set sensible defaults for optional parameters
- Don't require parameters that have obvious defaults
- Document what happens with default values

### 5. Error Handling
Return informative errors:
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "No customer found with email: test@example.com"
  }
}
```

## Implementation Patterns

### TypeScript MCP Server
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({
  name: "my-mcp-server",
  version: "1.0.0"
}, {
  capabilities: { tools: {} }
});

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "my_tool",
      description: "Description of what this tool does",
      inputSchema: { /* JSON Schema */ }
    }
  ]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  // Handle tool calls
  return { content: [{ type: "text", text: JSON.stringify(result) }] };
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

### Python MCP Server
```python
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("my-mcp-server")

@server.tool()
async def my_tool(query: str, limit: int = 10) -> str:
    """Description of what this tool does."""
    # Implementation
    return json.dumps(result)

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write)
```

## Testing MCP Servers
1. Unit test each tool handler
2. Test with Claude Desktop (local development)
3. Test with Claude Code (integration)
4. Edge cases: empty results, invalid input, API failures, timeouts
5. Performance: Response time under load

## Common MCP Use Cases
- CRM integration (search customers, create tickets)
- Database queries (read-only access to production data)
- Monitoring dashboards (fetch metrics, alert status)
- Code generation helpers (scaffolding, boilerplate)
- External API wrappers (Stripe, GitHub, Slack)
