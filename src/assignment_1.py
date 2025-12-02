import threading
import time
import queue
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%H:%M:%S')

class DataTransferSystem:
    def __init__(self, source_data, queue_size=5):
        # The Source Container (Requirement: "reads from a source container")
        self.source_container = source_data 
        
        # The Destination Container (Requirement: "stores items in a destination container")
        self.destination_container = []
        
        # Blocking Queue (Requirement: "Blocking queues", "Thread synchronization")
        self.shared_queue = queue.Queue(maxsize=queue_size)
        
        # Synchronization primitive
        self.lock = threading.Lock()

    def producer(self):
        """Reads from source container and adds to queue."""
        while True:
            item = None
            
            # critical section: safely pop from source container
            with self.lock:
                if not self.source_container:
                    break # Stop if source is empty
                item = self.source_container.pop(0)

            if item:
                try:
                    # put() blocks if queue is full (Requirement: Wait mechanism)
                    self.shared_queue.put(item, timeout=2)
                    logging.info(f"[PRODUCER] Transferred {item} to Queue")
                    time.sleep(0.1) # Simulate read time
                except queue.Full:
                    logging.warning("[PRODUCER] Queue full, waiting...")

    def consumer(self):
        """Reads from queue and stores in destination container."""
        while True:
            try:
                # get() blocks if queue is empty (Requirement: Wait/Notify)
                item = self.shared_queue.get(timeout=2)
                
                # Store in destination (Requirement: "stores items in a destination container")
                self.destination_container.append(item)
                logging.info(f"[CONSUMER] Stored {item} in Final Destination")
                
                self.shared_queue.task_done()
                time.sleep(0.2) # Simulate write time
            except queue.Empty:
                # If queue is empty and source is empty, we are done
                with self.lock:
                    if not self.source_container:
                        break

    def run_transfer(self):
        t1 = threading.Thread(target=self.producer)
        t2 = threading.Thread(target=self.consumer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()
        
        logging.info(f"Transfer Complete. Final Destination Count: {len(self.destination_container)}")
        return self.destination_container

if __name__ == "__main__":
    # Simulate a list of 10 items as the "Source Container"
    initial_data = [f"Record-{i}" for i in range(1, 11)]
    
    system = DataTransferSystem(initial_data)
    system.run_transfer()