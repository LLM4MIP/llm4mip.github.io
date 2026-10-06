"""Rebuild the current campaign; optionally rebuild the frozen skill downloads."""
import argparse
from build_campaign_data import main as build_campaign

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--include-skill',action='store_true',help='Also regenerate the separately frozen skill experiment downloads')
    args=parser.parse_args()
    build_campaign()
    if args.include_skill:
        from build_skill_data import main as build_skill
        build_skill()
