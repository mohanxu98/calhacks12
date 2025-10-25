"""
Temporal Worker for Button Analytics Workflows
This runs the Temporal worker that executes the workflows
"""

import asyncio
import logging
from temporalio.client import Client
from temporalio.worker import Worker
from temporal_workflows import (
    ButtonAnalyticsWorkflow,
    fetch_ga4_data,
    process_button_metrics,
    generate_button_insights,
    save_insights_to_database,
    send_insights_notification
)

async def main():
    """Start the Temporal worker"""
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Connect to Temporal server
    client = await Client.connect("localhost:7233")
    
    # Create worker
    worker = Worker(
        client,
        task_queue="button-analytics",
        workflows=[ButtonAnalyticsWorkflow],
        activities=[
            fetch_ga4_data,
            process_button_metrics,
            generate_button_insights,
            save_insights_to_database,
            send_insights_notification
        ]
    )
    
    logger.info("🚀 Starting Temporal worker for button analytics...")
    logger.info("📊 Worker will process GA4 button analytics workflows")
    logger.info("⏰ Worker is ready to execute workflows")
    
    # Run the worker
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
