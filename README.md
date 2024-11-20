# discord-database-bot# Discord Database Management Bot

A robust Discord bot for managing databases with automated backup functionality. This bot allows server administrators to create, manage, and automatically backup databases through simple Discord commands.

## Features

- ✨ Create new databases
- 🔄 Automated backup scheduling
  - Full backups
  - Differential backups
- 🔒 Server-specific database isolation
- 👤 Admin-only commands
- 📝 Ephemeral command responses for security

## Prerequisites

- Python 3.8 +
- discord.py library
- Async IO support
- Proper file system permissions

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your Discord bot token in config.py:
```python
TOKEN = 'your-bot-token-here'
```

## Usage

### Admin Commands

#### Create Database
Creates a new database with automated backup scheduling.

```
/create_db <db_name>
```

- `db_name`: Name of the database to create

The command will:
1. Verify server permissions
2. Create necessary folder structure
3. Initialize the database
4. Set up automated backup schedules
5. Create initial backup

### File Structure

```
Server_Name/
├── databases/
│   └── [database_name]
└── backups/
    ├── full/
    │   └── [database_name]_full_[timestamp]
    └── differential/
        └── [database_name]_diff_[timestamp]
```

## Backup System

### Full Backups
- Complete copy of the database
- Scheduled at regular intervals
- Stored in the `backups/full` directory

### Differential Backups
- Only backs up changes since the last full backup
- More frequent than full backups
- Stored in the `backups/differential` directory

## Error Handling

The bot implements robust error handling:
- Server verification
- Path existence validation
- Permission checks
- Graceful error messages

## Security Features

- Admin-only commands
- Ephemeral responses (only visible to command user)
- Server-specific database isolation
- Automated backup system

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request
