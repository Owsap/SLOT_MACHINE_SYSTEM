/// 1.
// Search
	case ITEM_SPECIAL:

// Add below
#if defined(__SLOT_MACHINE_SYSTEM__)
	{
		switch (item->GetVnum())
		{
		case ITEM_JACKPOT:
		{
			uint64_t iSocketValue = item->GetSocket(0);
			if (iSocketValue <= 0)
				return false;

			const uint64_t iTotalGold = GetGold() + iSocketValue;
			if (iTotalGold >= GOLD_MAX)
			{
				ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[Slot Machine] You're carying to much gold."));
				return false;
			}
			else
				PointChange(POINT_GOLD, iSocketValue);

			ITEM_MANAGER::instance().RemoveItem(item, "REMOVE (ITEM_JACKPOT)");
		}
		break;

		}
	}
	break;
#endif
