import subprocess

def print_terminal_output(command):
    # Open a subprocess and execute the command
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        universal_newlines=True  # Ensure output is text mode
    )

    # Read and print the output line by line in real-time
    for line in process.stdout:
        print(line, end='')

# Example command
command = "ollama run llama3 please tell me about linux "

# Call the function with the command
print_terminal_output(command)