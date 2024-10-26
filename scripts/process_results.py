import os
import matplotlib.pyplot as plt

def read_results(file_path):
    results = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                frame, count = line.strip().split(": ")
                results.append((frame, int(count)))
    except FileNotFoundError:
        print(f"Error: The results file was not found at {file_path}")
    except Exception as e:
        print(f"Error reading results file: {e}")
    return results
def plot_character_counts(results):
    if not results:
        print("No data to plot.")
        return

    frames = [x[0] for x in results]
    counts = [x[1] for x in results]

    # Find the frame(s) with the maximum character count
    max_count = max(counts)
    max_count_frames = [frames[i] for i, count in enumerate(counts) if count == max_count]

    # Calculate average characters per frame
    average_count = sum(counts) / len(counts) if counts else 0

    # Print information in the terminal
    print(f"Average number of characters per frame: {average_count:.2f}")
    print(f"The frame(s) with the highest character count of {max_count} is/are: {', '.join(max_count_frames)}")

    # Plot the data
    plt.figure(figsize=(15, 7))
    bars = plt.bar(frames, counts, color='skyblue')

    # Highlight the frames with the max character count in red
    for i, count in enumerate(counts):
        if count == max_count:
            bars[i].set_color('red')

    # Add text annotation for the frame(s) with the highest count
    for i, count in enumerate(counts):
        if count == max_count:
            plt.text(i, count + 0.5, f"Max: {count}\nFrame: {frames[i]}", ha='left', color='red', fontsize=10)

    # Display the average character count on the plot
    plt.text(0.01, 1.05, f"Average characters per frame: {average_count:.2f}", 
             transform=plt.gca().transAxes, color='green', fontsize=12)

    plt.xlabel('Frames', fontsize=12)
    plt.ylabel('Character Count', fontsize=12)
    
    # Move title upwards by adjusting the 'y' parameter
    plt.title('Character Count per Frame', fontsize=14, y=1.09)  # y=1.09 moves the title slightly upward

    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()

    # Adjust the layout to make space for text annotations
    plt.subplots_adjust(top=0.85)  # Increases top margin for better spacing

    # Show the plot
    plt.show()
if __name__ == "__main__":
    # Set the absolute path to detection_results.txt
    results_file = "C:/Users/Aastha Rajput/Desktop/anime-character-detection-aastharajput/outputs/detection_results.txt"

    print(f"Reading results from: {results_file}")
    results = read_results(results_file)
    plot_character_counts(results)


if __name__ == "__main__":
    # Set the absolute path to detection_results.txt
    results_file = "C:/Users/Aastha Rajput/Desktop/anime-character-detection-aastharajput/outputs/detection_results.txt"

    print(f"Reading results from: {results_file}")
    results = read_results(results_file)
    plot_character_counts(results)
