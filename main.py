def main():
    preferences = {
        "topics": [
            "Agent Building",
            "Practical AI Engineering Tutorials",
            "AI Products",
        ],
        "max_articles": 1,
        "reading_time_minutes": 2,
        "include_learning": True,
    }

    print("My AI News Agent")
    print("----------------")
    print("My interests:")

    for topic in preferences["topics"]:
        print(f"  - {topic}")

    print(f"\nMaximum articles per day: {preferences['max_articles']}")
    print(f"Reading time: up to {preferences['reading_time_minutes']} minutes")

    if preferences["include_learning"]:
        print("Includes a short AI engineering lesson")

    print("No relevant news? No email.")


if __name__ == "__main__":
    main()