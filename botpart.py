# Create a Database    
@admin.command(name="create_db", description="Create a new database")
    async def create_database(self, interaction: discord.Interaction, db_name: str) -> None:
        guild_id = interaction.guild.id
 
        ServerName = await asyncio.to_thread(utils.get_server_name, guild_id)
        if not ServerName:
            raise ValueError("Server not found in the database")
            
        BasePath = await asyncio.to_thread(utils.server_folder, ServerName)
        if not BasePath:
            raise ValueError(f"Server folder '{BasePath}' does not exist")
 
        PrimaryDatabasePath = await asyncio.to_thread(utils.primary_database_folder, BasePath, ServerName)
        if not PrimaryDatabasePath:
            raise ValueError(f"Folder path '{PrimaryDatabasePath}' does not exist")
        await asyncio.to_thread(utils.create_database, PrimaryDatabasePath, db_name, guild_id)
 
        scheduler = Scheduler(guild_id)
        print("Made Scheduler")
        await scheduler.start()
        print("Scheduler started")
        scheduler = self.set_scheduler(guild_id, self.schedulers)
        print("Scheduler set")
 
        await Scheduler.schedule_full_backup(scheduler, db_name)
        print("Added full backup to scheduler")
        await Scheduler.schedule_differential_backup(scheduler, db_name)
        print("Added differential backup to scheduler")
 
        BackupsRoute = await asyncio.to_thread(utils.backup_folder, BasePath, ServerName)
        if not BackupsRoute:
            raise ValueError(f"Backup Route: '{BackupsRoute}' does not exist")
        await asyncio.to_thread(utils.initial_backup_database, db_name, BackupsRoute)
            
        await interaction.response.send_message(f"Created database named: {db_name}", ephemeral=True)
